from fastapi import FastAPI

from app.routes import router as CarRouter

""" run with uvicorn
local dev run: poetry run uvicorn app.main:app --reload
"""

app = FastAPI()

app.include_router(CarRouter, tags=["Car"], prefix="/car")


@app.get("/", tags=["Root"])
async def read_root():
    return {"welcome": "to the root endpoint"}
