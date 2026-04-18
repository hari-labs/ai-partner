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
    return response.json()["response"]