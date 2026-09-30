from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI App")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/healthz")
def healthz():
    return {"status": "ok."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
