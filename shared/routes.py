from fastapi import FastAPI
from healthcheck import endpoints


def register_all_routes(app: FastAPI):
    app.include_router(endpoints.router)