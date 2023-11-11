import uvicorn
from fastapi import FastAPI, Header
from starlette.websockets import WebSocket
from typing import Optional
from fastapi import Depends, Header
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}

async def get_ws_current_user_id(token: str = Header()) -> Optional[int]:
    print(token)
    return 1

""" @app.websocket("/ws")
async def webocket_api(websocket: WebSocket,
                       user_id: Optional[int] = Depends(get_ws_current_user_id)):
    await websocket.accept()
    while True:
        input_text = await websocket.receive_text()
        await websocket.send({"message": input_text}) """

@app.websocket("/ws")
async def webocket_api(websocket: WebSocket,
                       user_id: Optional[int] = Depends(get_ws_current_user_id)):
    print(user_id)
    await websocket.accept()
    while True:
        input_text = await websocket.receive_text()
        await websocket.send({"message": input_text})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2000)