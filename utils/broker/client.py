import asyncio
import websockets
import config
import json


async def hello():
    uri = f"ws://{config.HOST}:{config.PORT}"
    async with websockets.connect(uri) as websocket:
        message = json.dumps(dict(
            client_type=config.SUBSCRIBER,
            content="Hi I am Nanda kishore. I would like to subscribe to channel 24"
        )).encode()
        greeting = await websocket.send(message)
        print(f"<<< {greeting}")

asyncio.run(hello())
