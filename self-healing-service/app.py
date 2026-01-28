from fastapi import FastAPI
from api.locator_api import router

app = FastAPI(title="LLM-Powered Locator Healing Service")
app.include_router(router, prefix="/locator")
