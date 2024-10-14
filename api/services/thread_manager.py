import asyncio
from typing import Dict, Set

from fastapi import WebSocket, WebSocketDisconnect


class ThreadManager:
    def __init__(self, thread_id: str, assistant_id: str):
        self.clients: Set[WebSocket] = set()
        self.queue: asyncio.Queue = asyncio.Queue()
        self.thread_id = thread_id
        self.assistant_id = assistant_id
        self.broadcast_task = asyncio.create_task(self.broadcast())

    async def broadcast(self):
        while True:
            message = await self.queue.get()
            print("Broadcasting message", message)
            disconnected_clients = []
            for client in self.clients:
                try:
                    print("Sending message to client")
                    print(len(message))
                    await client.send_text(message)
                except WebSocketDisconnect:
                    disconnected_clients.append(client)
            for client in disconnected_clients:
                self.clients.remove(client)
            self.queue.task_done()


thread_managers: Dict[str, ThreadManager] = {}
