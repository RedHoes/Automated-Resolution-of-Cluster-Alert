from fastapi import FastAPI
from api_v1.api.router import router as api_v1_router

app = FastAPI()

app.include_router(api_v1_router)
