import sys
from pathlib import Path

# Ensure project root is on sys.path to import 'app'
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from starlette.testclient import TestClient
from app.main import app


def main():
    client = TestClient(app)

    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, FastAPI!"}

    h = client.get("/healthz")
    assert h.status_code == 200
    assert h.json() == {"status": "ok"}

    print("Smoke test passed!")


if __name__ == "__main__":
    main()
