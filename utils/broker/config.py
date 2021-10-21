import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

HOST = "localhost"
PORT = 5678
SUBSCRIBER = "SUBSCRIBER"
PUBLISHER = "PUBLISHER"
