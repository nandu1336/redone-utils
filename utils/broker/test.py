from enum import Enum, auto
import json


class ClientType(Enum):
    SUBSCRIBER = auto()
    PUBLISHER = auto()

    print(SUBSCRIBER)
    print(PUBLISHER)


class Message:
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


print(Message(ClientType.SUBSCRIBER, "Hi I want to subscribe to the following channel",
              "ROAST").to_json())
