from fastapi import FastAPI

from app.api.webook import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running"}
