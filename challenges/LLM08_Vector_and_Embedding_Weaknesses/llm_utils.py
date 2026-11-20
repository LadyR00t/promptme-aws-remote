import os
from promptme_auth import make_ollama_client, ollama_base_url

OLLAMA_BASE = ollama_base_url(os.getenv("OLLAMA_BASE", "http://localhost:11434"))
PROMPTME_MODEL = os.getenv("PROMPTME_MODEL", "granite3.1-moe:1b")
_ollama_client = make_ollama_client(OLLAMA_BASE)

def query_llm(prompt: str, model: str = PROMPTME_MODEL) -> str:
    try:
        res = _ollama_client.generate(model=model, prompt=prompt)
        return res.get("response", "[No response]")
    except Exception as e:
        return f"[LLM Error]: {e}"
