# PromptMe con Ollama remoto autenticado (GCP)

Este proyecto usa la API nativa de Ollama (`/api/chat`, `/api/generate`) contra un endpoint remoto que **exige Bearer token**.

## Variables de entorno

```powershell
$env:PROMPTME_OLLAMA_BASE_URL="http://136.68.19.154:8080"
$env:PROMPTME_API_KEY="<LITELLM_MASTER_KEY>"
$env:PROMPTME_MODEL="aisecops"
$env:PROMPTME_GUARDIAN_MODEL="aisecops"
$env:PROMPTME_SQL_MODEL="aisecops"
```

Notas:
- `PROMPTME_OLLAMA_BASE_URL`: URL pública del proxy autenticado (no el puerto crudo 11434).
- `PROMPTME_API_KEY`: token Bearer (mismo valor que `LITELLM_MASTER_KEY`). También acepta `LITELLM_MASTER_KEY` como fallback.
- Sin token el backend responde `401`.

## Ejecución

```powershell
pip install -r requirements.txt
python main.py
```

## OpenAI-compatible (Euskalhack / otros clientes)

Si prefieres API tipo OpenAI:

- Base URL: `http://136.82.165.140/v1`
- Model: `aisecops`
- Auth: `Authorization: Bearer <LITELLM_MASTER_KEY>`
