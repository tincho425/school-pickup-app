import asyncpg
from fastapi import FastAPI
import os

from api.routers.student import router as student_router
from .config import DATABASE_URL_SYNC

app = FastAPI()

async def connect_to_db():
    return await asyncpg.connect(dsn=DATABASE_URL_SYNC)

def main() -> None:
    print("Hello from api!")

@app.get("/health")
async def health_check() -> dict:
    try:
        conn = await connect_to_db()
        await conn.fetchval("SELECT 1")
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "message": str(e)}
    finally:
        if 'conn' in locals() and not conn.is_closed():
            await conn.close()
      
app.include_router(student_router)