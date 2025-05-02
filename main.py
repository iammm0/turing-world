from fastapi import FastAPI
from config import settings
from app.shared.dependencies import lifespan_handler
from app.shared.routes import register_all_routes

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan_handler  # 初始化数据库等资源
)

# 注册所有模块的路由
register_all_routes(app)