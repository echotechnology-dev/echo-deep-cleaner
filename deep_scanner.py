import os

# ❌ Абсолютно запрещённые пути (никогда не трогаем)
FORBIDDEN_KEYWORDS = (
    r"\windows",
    r"\system32",
    r"\program files",
    r"\program files (x86)",
    r"\programs",
    r"\python",
    r"\pip",
    r"\microsoft",
    r"\google",
    r"\mozilla",
    r"\user data",
    r"\profiles",
    r"\extensions",
    r"\local storage",
    r"\indexeddb",
    r"\service worker",
    r"\node_modules",
    r"\vscode",
    r"\code\user",
)

# ✅ Разрешённые ТОЛЬКО cache-папки
SAFE_CACHE_FOLDERS = (
    "cache",
    "code cache",
    "gpucache",
    "crashpad",
    "shadercache",
    "temp",
    "logs",
)

def is_safe_cache_path(path: str) -> bool:
    p = path.lower()

    # жёсткий запрет
    for forbidden in FORBIDDEN_KEYWORDS:
        if forbidden in p:
            return False

    # разрешаем ТОЛЬКО кэш
    return any(folder in p for folder in SAFE_CACHE_FOLDERS)


def scan_directory(base_path: str):
    results = []

    for root, dirs, files in os.walk(base_path):
        if not is_safe_cache_path(root):
            continue

        for file in files:
            path = os.path.join(root, file)

            try:
                size = os.path.getsize(path)
                if size == 0:
                    continue

                results.append({
                    "path": path,
                    "size": round(size / (1024 * 1024), 2)
                })

            except:
                continue

    return results
