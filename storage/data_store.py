import json
import os
from datetime import datetime

DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

def save_round(player, computer, winner):
    ensure_data_dir()

    now = datetime.now().isoformat()
    entry = {
        "timestamp": now,
        "player": player,
        "computer": computer,
        "winner": winner
    }

    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            history = []

    history.append(entry)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

def get_history(limit=None):
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    return history if limit is None else history[-limit:]

# Espacio para estadísticas
