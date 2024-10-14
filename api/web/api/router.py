from fastapi.routing import APIRouter

from api.web.api import assistants, auth, docs, monitoring, threads, websocket

api_router = APIRouter()
api_router.include_router(docs.router)

api_router.include_router(monitoring.router, tags=["Monitoring"])

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users.router, prefix = "/users", tags = [ "Users" ])

api_router.include_router(assistants.router, prefix="/assistants")
api_router.include_router(threads.router, prefix="/threads")
api_router.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])
