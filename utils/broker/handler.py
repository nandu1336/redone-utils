import json
# from config import logger
import logging as logger

from utils.broker import config

subscribers = set()
publishers = set()


async def socket_handler(connection, request_path):
    logger.info("second parameter:{}".format(request_path))
    # logger.info("connection.__dict__:{}".format(connection.__dict__))
    async for message in connection:
        await process(message, connection)

    pass


async def process(message, connection):
    print("message in process:", message)
    if isinstance(message, bytes):
        message = message.decode()
        if "{" in message:
            message = json.loads(message)
            print("message after parsing:", message,
                  message['client_type'], message['client_type'] == config.SUBSCRIBER)
            if message['client_type'] == config.SUBSCRIBER:
                print(
                    "invoking register-subscriber with {}, {}".format(message, connection))
                await register_subscriber(message, connection)
            elif message['client_type'] == config.PUBLISHER:
                await register_publisher(message, connection)


async def register_subscriber(message, connection):
    logger.info("register_subscriber invoked with:{}, {}".format(
        message, connection))
    if connection:
        subscribers.add(connection)
    pass


async def register_publisher(message, connection):
    pass


async def handle_new_subscription(message, connection):
    logger.info("hanlde_new_subscription invoked with:{}, {}".format(
        message, connection))
    pass


async def handle_new_publishing(message, connection):
    logger.info("hanlde_new_publishing invoked with:{}, {}".format(
        message, connection))
    pass
