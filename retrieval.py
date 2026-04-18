import re
import json

def extract_keywords(text):
    stopwords = ["i", "me", "my", "we", "you", "the", "a", "an", "and", "or", "is", "are", "was", "were", "to", "of", "in", "on", "for", "with", "that", "this", "it", "am", "can", "really"]

    text = text.lower()
    
    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    words = text.split()
    
    keywords = [word for word in words if word not in stopwords]
    
    return keywords


def search_memory(keywords):
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
    except:
        return []

    results = []

    for line in memory:
        line_lower = line.lower()
        for word in keywords:
            if word in line_lower:
                results.append(line)
                break

    return results[-5:]  # take last 5 relevant

