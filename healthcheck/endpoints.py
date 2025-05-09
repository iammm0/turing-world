from fastapi import APIRouter
from shared.db import redis_client, qdrant_client, get_db_session
from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/health", tags=["Health Check"])

@router.get("/postgres")
async def check_postgres(session: AsyncSession = Depends(get_db_session)):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok", "db": "postgres"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@router.get("/redis")
async def check_redis():
    try:
        pong = await redis_client.ping()
        return {"status": "ok", "response": pong}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@router.get("/qdrant")
async def check_qdrant():
    try:
        collections = await qdrant_client.get_collections()
        return {"status": "ok", "collections": collections}
    except Exception as e:
        return {"status": "error", "error": str(e)}
