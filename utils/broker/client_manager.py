from exceptions import NoSuchChannelFound


class ClientManager:
    def __init__(self):
        self.list_of_subscribers = []
        self.list_of_channels = []
        self.channels = {}

    def subscribe(self, channel, connection):
        if channel in self.channels:
            self.channels[channel].append(connection)
        else:
            self.channels[channel] = [connection]

        return True

    def unsubscribe(self, channel, connection):
        if channel in self.channels:
            self.channels[channel].remove(connection)
        else:
            raise NoSuchChannelFound(channel)

        return True

    def publish(self, channel, message):
        if channel in self.channels:
            subscribers = self.channels[channel]
            pass
