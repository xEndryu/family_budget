from fastapi import FastAPI
from fastapi_pagination import add_pagination

from .api.base import api_router
from .db.base import Base
from .db.session import engine
from .helpers.config import settings


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def enable_pagination(app):
    add_pagination(app)


def startup():
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
    include_router(app)
    create_tables()
    enable_pagination(app)
    return app


app = startup()
