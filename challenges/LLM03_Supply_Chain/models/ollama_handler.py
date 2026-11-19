import requests
import os

OLLAMA_URL = os.getenv("PROMPTME_OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")

def generate_with_ollama(model_name, history, prompt):
    # Send the chat to Ollama's API
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": model_name,
            "messages": history + [{"role": "user", "content": prompt}],
            "stream": False
            
        }
    )
    response.raise_for_status()
    result = response.json()
    return result["message"]["content"]
