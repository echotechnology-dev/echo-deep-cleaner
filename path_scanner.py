import os

def scan_path(base_path, risk="Review"):
    results = []

    for root, _, files in os.walk(base_path):
        for file in files:
            path = os.path.join(root, file)
            try:
                size = os.path.getsize(path)
                if size == 0:
                    continue

                results.append({
                    "type": "File",
                    "path": path,
                    "size": round(size / (1024 * 1024), 2),
                    "risk": risk
                })
            except:
                pass

    return results
