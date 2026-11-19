import os
import ollama

OLLAMA_BASE = os.getenv("PROMPTME_OLLAMA_BASE_URL", os.getenv("OLLAMA_BASE", "http://localhost:11434"))
PROMPTME_MODEL = os.getenv("PROMPTME_MODEL", "granite3.1-moe:1b")

def query_llm(prompt: str, model: str = PROMPTME_MODEL) -> str:
    try:
        res = ollama.generate(model=model, prompt=prompt, options={"base_url": OLLAMA_BASE})
        return res.get("response", "[No response]")
    except Exception as e:
        return f"[LLM Error]: {e}"
