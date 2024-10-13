from fastapi.routing import APIRouter

from api.web.api import auth, docs, dummy, echo, monitoring

api_router = APIRouter()
api_router.include_router(docs.router)

api_router.include_router(monitoring.router, tags=["Monitoring"])
api_router.include_router(echo.router, prefix="/echo", tags=["Echo"])

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users.router, prefix = "/users", tags = [ "Users" ])

api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
