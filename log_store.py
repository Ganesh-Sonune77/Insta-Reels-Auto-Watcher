import threading
import json
import os
from datetime import datetime

log_data = {}
log_lock = threading.Lock()

def log(screen_id, message):
    with log_lock:
        if screen_id not in log_data:
            log_data[screen_id] = []
        log_data[screen_id].append(message)

def get_logs():
    with log_lock:
        return dict(log_data)

def save_logs_to_file():
    with log_lock:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("logs", exist_ok=True)
        with open(f"logs/session_{timestamp}.json", "w") as f:
            json.dump(log_data, f, indent=4)