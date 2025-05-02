from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.shared.db import engine
from app.shared.db import Base  # 用于创建表结构

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    # 服务器启动前（可初始化数据库）
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield