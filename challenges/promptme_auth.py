"""Auth helpers for remote Ollama endpoints that require Bearer token."""
from __future__ import annotations

import os
from typing import Any, Dict, Optional


def ollama_base_url(default: str = "http://localhost:11434") -> str:
    return os.getenv("PROMPTME_OLLAMA_BASE_URL", default).rstrip("/")


def ollama_api_key() -> str:
    # Prefer PromptMe-specific key; fall back to shared LiteLLM master key.
    return (
        os.getenv("PROMPTME_API_KEY")
        or os.getenv("LITELLM_MASTER_KEY")
        or ""
    ).strip()


def ollama_headers() -> Dict[str, str]:
    key = ollama_api_key()
    if not key:
        return {}
    if key.lower().startswith("bearer "):
        return {"Authorization": key}
    return {"Authorization": f"Bearer {key}"}


def make_ollama_client(host: Optional[str] = None):
    import ollama

    kwargs: Dict[str, Any] = {"host": host or ollama_base_url()}
    headers = ollama_headers()
    if headers:
        kwargs["headers"] = headers
    return ollama.Client(**kwargs)


def make_chat_ollama(**kwargs):
    from langchain_ollama import ChatOllama

    client_kwargs = dict(kwargs.pop("client_kwargs", None) or {})
    headers = ollama_headers()
    if headers:
        client_kwargs["headers"] = {**client_kwargs.get("headers", {}), **headers}
    base_url = kwargs.pop("base_url", None) or ollama_base_url()
    return ChatOllama(base_url=base_url, client_kwargs=client_kwargs, **kwargs)


def make_ollama_llm(**kwargs):
    from langchain_ollama import OllamaLLM

    client_kwargs = dict(kwargs.pop("client_kwargs", None) or {})
    headers = ollama_headers()
    if headers:
        client_kwargs["headers"] = {**client_kwargs.get("headers", {}), **headers}
    base_url = kwargs.pop("base_url", None) or ollama_base_url()
    return OllamaLLM(base_url=base_url, client_kwargs=client_kwargs, **kwargs)
