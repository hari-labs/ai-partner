import requests

def summarize_text(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Summarize this conversation briefly:\n{text}",
            "stream": False
        }
    )
    
    data = response.json()
    
    # safe handling
    if "response" in data:
        return data["response"]
    else:
        print("Summary error:", data)
        return "Summary not available."