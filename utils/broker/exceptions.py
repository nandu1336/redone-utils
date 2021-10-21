class NoSuchChannelFound(Exception):
    def __init__(self, channel) -> None:
        super().__init__((channel))
        self.exception = f"No channel with name {channel} found in the list."
