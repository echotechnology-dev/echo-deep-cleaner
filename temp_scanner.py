import os
import tempfile

def scan_temp():
    results = []
    temp_dir = tempfile.gettempdir()

    for root, _, files in os.walk(temp_dir):
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
                pass

    return results
