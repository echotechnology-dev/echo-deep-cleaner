from datetime import datetime

def log(message: str):
    with open("cleaner.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")
