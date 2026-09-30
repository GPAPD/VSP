# Simple FastAPI App

A minimal FastAPI service with a health check and a hello endpoint.

## Quick start (local)

```bash
# (optional) create and activate a venv
python -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the app
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Endpoints:
- `GET /` → `{ "message": "Hello, FastAPI!" }`
- `GET /healthz` → `{ "status": "ok" }`

## Smoke test

```bash
python tests/smoke_test.py
```

## Docker

```bash
# build
docker build -t simple-fastapi:latest .
# run
docker run --rm -p 8000:8000 simple-fastapi:latest
```
