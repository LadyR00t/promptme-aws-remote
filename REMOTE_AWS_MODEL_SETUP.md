# Remote Ollama setup (shared GCP endpoint)

Use this when you want to run PromptMe on your laptop without installing Ollama locally.

## Endpoint

| Item | Value |
|---|---|
| Ollama base URL | `http://136.68.19.154:8080` |
| Auth | `Authorization: Bearer <TOKEN>` |
| Env var for token | `PROMPTME_API_KEY` (fallback: `LITELLM_MASTER_KEY`) |

Ask the workshop organizer for the token. Do not commit it to git.

## Environment variables

### PowerShell

```powershell
$env:PROMPTME_OLLAMA_BASE_URL="http://136.68.19.154:8080"
$env:PROMPTME_API_KEY="<TOKEN_DEL_TALLER>"
$env:PROMPTME_MODEL="mistral"
$env:PROMPTME_GUARDIAN_MODEL="granite3-guardian"
$env:PROMPTME_SQL_MODEL="sqlcoder"
```

### Bash

```bash
export PROMPTME_OLLAMA_BASE_URL="http://136.68.19.154:8080"
export PROMPTME_API_KEY="<TOKEN_DEL_TALLER>"
export PROMPTME_MODEL="mistral"
export PROMPTME_GUARDIAN_MODEL="granite3-guardian"
export PROMPTME_SQL_MODEL="sqlcoder"
```

## Run

```bash
pip install -r requirements.txt
python main.py
```

Open http://127.0.0.1:5000

## Available models on the shared backend

- `mistral` (default app model)
- `llama3`
- `sqlcoder` (LLM05)
- `granite3.1-moe:1b` (LLM08)
- `granite3-guardian` (LLM01 guardian)
- `aisecops` (optional custom model)

## Quick connectivity check

```powershell
curl.exe http://136.68.19.154:8080/api/tags -H "Authorization: Bearer $env:PROMPTME_API_KEY"
```

Expected: JSON with the model list. Without token: `401`.

## Related OpenAI-compatible endpoint (Euskalhack / other clients)

| Item | Value |
|---|---|
| Base URL | `http://136.82.165.140/v1` |
| Model | `aisecops` (or `current`) |
| Auth | Bearer token (same workshop token) |
