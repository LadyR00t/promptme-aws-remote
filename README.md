# PromptMe - A Vulnerable LLM Application (remote-ready)

<p>
<img src="https://github.com/OWASP/www-project-promptme/blob/main/static/logo.png?raw=true" width="600" alt="Thumbnail"/>
</p>

Vulnerable LLM lab based on OWASP Top 10 for LLM Applications (10 CTF-style challenges).

This fork is prepared to run against a **shared remote Ollama endpoint** (with Bearer auth). You do **not** need to install Ollama or download models on your laptop.

## Quick start (recommended)

### Prerequisites
- Python 3.10+
- `pip`
- The shared API token from the workshop organizer (`PROMPTME_API_KEY`)

### 1) Clone

```bash
git clone https://github.com/LadyR00t/promptme-aws-remote.git
cd promptme-aws-remote
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure remote models + token

**PowerShell (Windows):**

```powershell
$env:PROMPTME_OLLAMA_BASE_URL="http://136.68.19.154:8080"
$env:PROMPTME_API_KEY="<TOKEN_DEL_TALLER>"
$env:PROMPTME_MODEL="mistral"
$env:PROMPTME_GUARDIAN_MODEL="granite3-guardian"
$env:PROMPTME_SQL_MODEL="sqlcoder"
```

**Bash (Linux/macOS):**

```bash
export PROMPTME_OLLAMA_BASE_URL="http://136.68.19.154:8080"
export PROMPTME_API_KEY="<TOKEN_DEL_TALLER>"
export PROMPTME_MODEL="mistral"
export PROMPTME_GUARDIAN_MODEL="granite3-guardian"
export PROMPTME_SQL_MODEL="sqlcoder"
```

Models already available on the shared backend:
- `mistral`
- `llama3`
- `sqlcoder`
- `granite3.1-moe:1b`
- `granite3-guardian`
- `aisecops` (extra custom model)

Without `PROMPTME_API_KEY` the remote API returns `401`.

### 4) Run

```bash
python main.py
```

Open: http://127.0.0.1:5000

Click **Start** on a challenge (e.g. LLM01).

More details: [REMOTE_AWS_MODEL_SETUP.md](REMOTE_AWS_MODEL_SETUP.md)

---

## Optional: run with local Ollama

Only if you prefer local models instead of the shared endpoint.

1. Install Ollama: https://ollama.com/download
2. Pull models:

```bash
ollama serve
ollama pull mistral
ollama pull llama3
ollama pull sqlcoder
ollama pull granite3.1-moe:1b
ollama pull granite3-guardian
```

3. Point env to localhost (no API key needed for local default):

```powershell
$env:PROMPTME_OLLAMA_BASE_URL="http://localhost:11434"
$env:PROMPTME_MODEL="mistral"
$env:PROMPTME_GUARDIAN_MODEL="granite3-guardian"
$env:PROMPTME_SQL_MODEL="sqlcoder"
Remove-Item Env:PROMPTME_API_KEY -ErrorAction SilentlyContinue
python main.py
```

---

## Tests

```bash
python -m pytest -q
```

## Spoilers

Challenge solutions (upstream OWASP):  
https://github.com/OWASP/www-project-promptme/tree/main/solutions

## Disclaimer

PromptMe is intentionally vulnerable and for education only. Run it in a sandbox/VM when possible. Do not reuse these insecure patterns in production.

## Contributing

Fork, branch, commit, and open a Pull Request.
