import os

COMMON_PATHS = [
    os.getenv("APPDATA"),
    os.getenv("LOCALAPPDATA"),
    "C:\\Program Files",
    "C:\\Program Files (x86)"
]

def scan_leftovers():
    results = []

    for base in COMMON_PATHS:
        if not base or not os.path.exists(base):
            continue

        for name in os.listdir(base):
            path = os.path.join(base, name)
            if os.path.isdir(path):
                # логика проверки "мертвой" папки позже
                results.append({
                    "type": "Leftover",
                    "path": path,
                    "size": 0,
                    "risk": "Review"
                })

    return results
