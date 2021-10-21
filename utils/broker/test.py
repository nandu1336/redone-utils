from enum import Enum, auto
import json


class ClientType(Enum):
    SUBSCRIBER = auto()
    PUBLISHER = auto()


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

            if k == "content":
                complex_keys = [k for k in self.content.keys(
                ) if isinstance(self.content[k], object)]
                for key in complex_keys:
                    if isinstance(self.content, dict):
                        pass

            else:
                j[k] = self.__dict__[k]
        return json.dumps(j)

    def dict_to_string(self, d):
        for key in d.keys():
            if isinstance(d[key], str):
                return json.dumps(d)
            if isinstance(d[key], dict):
                return self.dict_to_string(d[key])


print(Message(ClientType.SUBSCRIBER, "Hi I want to subscribe to the following channel",
              "ROAST").to_json())
