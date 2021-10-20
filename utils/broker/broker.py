import asyncio
import websockets
# from config import logger
import logging as logger
import config
import logging
import json


class Broker:
    def __init__(self, host, port):
        self.host = host or config.HOST
        self.port = port or config.PORT
        self.subscribers = set()
        self.publishers = set()

    async def serve(self):
        logger.info("Starting broker.")
        async with websockets.serve(self.socket_handler, self.host, self.port):
            logger.info("Broker listening on port {}".format(self.port))
            await asyncio.Future()  # run forever

    async def socket_handler(self, connection, request_path):
        logger.info("second parameter:{}".format(request_path))
        async for message in connection:
            await self.process(message, connection)

    async def process(self, message, connection):
        logging.info("message in process:", message)

        if isinstance(message, bytes):
            message = message.decode()

        if "{" in message:
            message = json.loads(message)
            print("message after parsing:", message,
                  message['client_type'], message['client_type'] == config.SUBSCRIBER)
            if message['client_type'] == config.SUBSCRIBER:
                print(
                    "invoking register-subscriber with {}, {}".format(message, connection))
                await self.register_subscriber(message, connection)
            elif message['client_type'] == config.PUBLISHER:
                await self.register_publisher(message, connection)

    def register_subscriber(self, message, connection):


asyncio.run(Broker().serve())
