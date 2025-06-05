from fastapi import APIRouter
from listening_ripples.users import api as user_api

# from app.api.routes import items, login, private, users, utils
from ..config import settings

api_router = APIRouter()
# api_router.include_router(login.router)
api_router.include_router(user_api.router)
# api_router.include_router(utils.router)
# api_router.include_router(items.router)


# if settings.ENVIRONMENT == "local":
#     api_router.include_router(private.router)