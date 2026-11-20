import requests
from promptme_auth import ollama_base_url, ollama_headers

OLLAMA_URL = ollama_base_url()

def generate_with_ollama(model_name, history, prompt):
    # Send the chat to Ollama's API
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        headers=ollama_headers(),
        json={
            "model": model_name,
            "messages": history + [{"role": "user", "content": prompt}],
            "stream": False
            
        }
    )
    response.raise_for_status()
    result = response.json()
    return result["message"]["content"]
