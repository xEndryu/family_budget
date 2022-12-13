from fastapi import APIRouter

from .v1 import budgets, health, login, users, version

api_router = APIRouter()
api_router.include_router(budgets.router, prefix="/api/v1/budgets", tags=["budgets"])
api_router.include_router(health.router, prefix="/api/v1/health", tags=["health"])
api_router.include_router(users.router, prefix="/api/v1/users", tags=["users"])
api_router.include_router(version.router, prefix="/ap1/v1/version", tags=["version"])
api_router.include_router(login.router, prefix="/api/v1/login", tags=["login"])
