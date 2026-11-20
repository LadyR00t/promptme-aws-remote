import os
from promptme_auth import make_ollama_client, ollama_base_url

OLLAMA_BASE_URL = ollama_base_url()
PROMPTME_MODEL = os.getenv("PROMPTME_MODEL", "mistral")
ollama_client = make_ollama_client(OLLAMA_BASE_URL)

def query_llm(prompt):
    response = ollama_client.chat(model=PROMPTME_MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
