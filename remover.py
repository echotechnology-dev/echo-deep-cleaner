import os
import shutil

def remove_path(path):
    if not os.path.exists(path):
        return False, "Path not found"

    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            if not os.listdir(path):
                return False, "Empty folder"
            shutil.rmtree(path)

        return True, "Removed"

    except PermissionError:
        return False, "Access denied"
    except Exception:
        return False, "In use or locked"
