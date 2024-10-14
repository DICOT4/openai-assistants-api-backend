import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from api.services.thread_manager import ThreadManager, thread_managers

router = APIRouter()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket, thread_id: str, assistant_id: str):
    await websocket.accept()
    if thread_id not in thread_managers:
        thread_managers[thread_id] = ThreadManager(thread_id, assistant_id)
    thread_manager = thread_managers[thread_id]
    thread_manager.clients.add(websocket)
    try:
        while True:
            # Keep the connection alive
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        thread_manager.clients.remove(websocket)
        await websocket.close()
    except Exception:
        thread_manager.clients.remove(websocket)
        await websocket.close()
