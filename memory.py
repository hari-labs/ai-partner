import json
import re

def save_memory(chat_history):
    with open("memory.json", "w") as f:
        json.dump(chat_history, f)

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return []
    
import json
import re

def store_facts(facts_response):
    # Extract JSON part
    match = re.search(r'\{.*\}', facts_response, re.DOTALL)

    if match:
        json_text = match.group()
    else:
        json_text = "{}"

    # Parse safely
    try:
        new_facts = json.loads(json_text)
    except:
        new_facts = {}

    if not new_facts:
        return  # nothing to store

    # Load existing facts
    try:
        with open("facts.json", "r") as f:
            existing_facts = json.load(f)
    except:
        existing_facts = {}

    # Merge (update dictionary)
    existing_facts.update(new_facts)

    # Save back
    with open("facts.json", "w") as f:
        json.dump(existing_facts, f, indent=2)