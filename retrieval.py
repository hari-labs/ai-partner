import re
import json

def extract_keywords(text):
    stopwords = ["i", "me", "my", "we", "you", "the", "a", "an", "and", "or", "is", "are", "was", "were", "to", "of", "in", "on", "for", "with", "that", "this", "it", "am", "can", "really"]

    text = text.lower()
    
    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    words = text.split()
    
    keywords = [word for word in words if word not in stopwords]

    # filter very short words
    keywords = [word for word in keywords if len(word) > 3]
    
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
        score = sum(word in line_lower for word in keywords)
        if score >= 2:
            results.append(line)

    return results[-5:]  # take last 5 relevant
    

def is_fact_statement(text):
    text = text.lower()

    # preference / identity patterns
    if any(k in text for k in ["i like", "i love", "my favorite", "i prefer"]):
        return True

    if " is " in text:
        # reject temporary/conditional tone
        if any(k in text for k in ["if", "when", "today", "tomorrow", "now", "currently"]):
            return False

        # reject ongoing states (ing words)
        if "ing" in text:
            return False

        return True

    return False