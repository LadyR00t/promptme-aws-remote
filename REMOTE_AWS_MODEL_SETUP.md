# PromptMe usando modelos en AWS (sin Ollama local)

Este proyecto quedó preparado para usar un endpoint de Ollama remoto en AWS.

## Variables de entorno

Antes de ejecutar cualquier challenge, define:

```powershell
$env:PROMPTME_OLLAMA_BASE_URL="http://<IP_O_HOST_AWS>:11434"
$env:PROMPTME_MODEL="aisecops"
$env:PROMPTME_GUARDIAN_MODEL="aisecops"
$env:PROMPTME_SQL_MODEL="aisecops"
```

Notas:
- `PROMPTME_OLLAMA_BASE_URL`: URL base de tu instancia AWS con Ollama (sin `/api/...`).
- `PROMPTME_MODEL`: modelo principal.
- `PROMPTME_GUARDIAN_MODEL`: challenge LLM01 usa un segundo modelo para "guardian". Si no tienes uno dedicado, usa el mismo.
- `PROMPTME_SQL_MODEL`: challenge LLM05.

## Ejecución

```powershell
pip install -r requirements.txt
python main.py
```

## Si quieres alternar entre dos modelos en AWS

Puedes cambiar solo:

```powershell
$env:PROMPTME_MODEL="otro-modelo"
```

y reiniciar el challenge.

## Limitación importante

PromptMe usa API de Ollama (`/api/chat` y `/api/generate`).  
Para usar modelos en AWS con este proyecto sin cambios adicionales, el backend debe exponer interfaz de Ollama.
