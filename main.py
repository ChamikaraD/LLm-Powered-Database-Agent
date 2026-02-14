from fastapi import FastAPI

from user_router import router as user_router

app = FastAPI(title="LLM Powered Database Agent")

app.include_router(user_router)