import json

def save_memory(chat_history):
    with open("memory.json", "w") as f:
        json.dump(chat_history, f)

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return []