import asyncio
import websockets
import config
import logging
import json
from config import logger

import time


class Broker:
    def __init__(self, host=None, port=None):
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

        await connection.send("Hey welcome !!!")
        async for message in connection:
            print("message after parsing:", message)

            if isinstance(message, bytes):
                message = message.decode()

            if "{" in message:
                message = json.loads(message)

                if message['client_type'] == config.SUBSCRIBER:
                    await self.register_subscriber(message, connection)

                elif message['client_type'] == config.PUBLISHER:
                    await self.publish(message, connection)

    async def process_message(self, message):
        logging.info("message in process:", message)

        return message

    async def register_subscriber(self, message, connection):
        channel = message['channel']
        logger.info("New subscriber added to {}".format(channel))
        if connection:
            self.subscribers.add(connection)
        pass

    async def publish(self, message, connection):
        logger.info("Publishing to {}".format(message['channel']))
        if connection:
            self.broadcast(message)
        pass


asyncio.run(Broker().serve())
