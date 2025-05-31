from fastapi import FastAPI
from app.api.v1 import user

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

app.include_router(user.router, prefix="/api/v1", tags=["User"])


