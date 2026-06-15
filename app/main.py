from fastapi import FastAPI

from app.routes.sentiment_routes import router

from app.database.db import engine

from app.database.model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)