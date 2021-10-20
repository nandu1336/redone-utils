import json
from enum import Enum, auto


class ClientType(Enum):
    SUBSCRIBER = auto()
    PUBLISHER = auto()


class PayLoad:
    def __init__(self, client_type, content=None, channel=None):
        self.client_type = client_type
        self.content = content or ""
        self.channel = channel or ""
        pass

    def to_json(self):
        j = {}
        for k in self.__dict__:
            if k == "client_type":
                j[k] = "SUBSCRIBER" if self.client_type == ClientType.SUBSCRIBER else "PUBLISHER"
            else:
                j[k] = self.__dict__[k]
        return json.dumps(j)


def make_message(client_type=ClientType.PUBLISHER, content=None, channel=None):
    return PayLoad(client_type, content, channel).to_json()


def publish(content, channel):
    return PayLoad(ClientType.PUBLISHER, content=content, channel=channel)
