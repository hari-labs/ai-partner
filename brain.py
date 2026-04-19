import requests
from memory import save_memory, load_memory
from emotion import detect_uncertainty, detect_excitement, detect_frustration, detect_confusion
from summary import summarize_text
from retrieval import extract_keywords, search_memory, is_fact_statement

def chat_with_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


system_prompt = """
You are a helpful AI assistant.

Rules:
- No roleplay actions (no *smiles*, *leans*)
- No unnecessary drama
- Keep responses natural and clear
- Do not assume things without context
- If a reference (like "she", "it") is unclear, ask for clarification
- Use provided memory and facts carefully
- Avoid repeating the same question
"""

prompt_for_facts = """
Extract ONLY personal facts from the text.

Return STRICT JSON format:
{
  "key": "value"
}

Rules:
- No explanation
- No extra text
- Only JSON

Text:
{user_input}"""

chat_history = load_memory()

while True:
    user_input = input("You: ")

    if is_fact_statement(user_input):
        prompt_for_facts = prompt_for_facts.format(user_input=user_input)
        facts_response = chat_with_ollama(prompt_for_facts)
        print("Extracted facts:", facts_response)

    if detect_frustration(user_input):
        user_input += "\nNote: User seems frustrated. Respond calmly and help clearly."

    elif detect_confusion(user_input):
        user_input += "\nNote: User is confused. Explain step-by-step."

    elif detect_uncertainty(user_input):
        user_input += "\nNote: User seems uncertain. Ask a gentle follow-up question."

    elif detect_excitement(user_input):
        user_input += "\nNote: User is excited. Respond with enthusiasm."

    keywords = extract_keywords(user_input)
    relevant_memory = search_memory(keywords)
    memory_context = "\n".join(relevant_memory)

    if not relevant_memory:
        recent_context = "\n".join(chat_history[-3:])  # keep only recent
    else:
        recent_context = "\n".join(chat_history[-5:])  # last 5 messages

    if len(chat_history) > 20:
        old_part = "\n".join(chat_history[:10])
        
        summary = summarize_text(old_part)
        
        if summary != "Summary not available.":
            chat_history = [f"Summary: {summary}"] + chat_history[10:]

    full_prompt = system_prompt + "\n"
    
    if memory_context:
        full_prompt += "Relevant past memory:\n" + memory_context + "\n"

    full_prompt += "Recent conversation:\n" + recent_context + "\n"
    full_prompt += "User: " + user_input

    chat_history.append("User: " + user_input)
    response = chat_with_ollama(full_prompt)
    chat_history.append("AI: " + response)

    save_memory(chat_history)
    print("AI:", response)