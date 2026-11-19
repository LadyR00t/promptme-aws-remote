import ollama
import os

OLLAMA_BASE_URL = os.getenv("PROMPTME_OLLAMA_BASE_URL", "http://localhost:11434")
PROMPTME_MODEL = os.getenv("PROMPTME_MODEL", "mistral")
ollama_client = ollama.Client(host=OLLAMA_BASE_URL)

def query_llm(prompt):
    response = ollama_client.chat(model=PROMPTME_MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
