from .storage import FileStorage

"""
    Storages:
        ->  A storage is essentially a class that exposes set, get, save, clear and clear_saved_records methods. 
        ->  The values can be stored in either a database, or in memory, in a file or anyother possible way.
"""


class Session:
    """ 
        Session class should have methods to set session keys and values,
        get method to retreive the set values,
        clear method to clear all the values previously set.
    """

    def __init__(self, storage=None, expiry=None):
        self.storage = storage or FileStorage()
        self.expiry = expiry

    def get(self, key):
        return self.storage.get(key)

    def set(self, key, value):
        try:
            self.storage.set(key, value)
            return True
        except:
            return False

    def clear(self):
        try:
            self.storage.clear()
            return True
        except:
            return False

    # def save(self):
    #     try:
    #         self.storage.save()
    #         return True
    #     except:
    #         return False

    # def clear_snapshot(self):
    #     try:
    #         self.storage.clear(clear_snapshot=True)
    #         return True
    #     except:
    #         return False


if __name__ == "__main__":
    s = Session()

    while True:
        user_input = input(">>>")
        if user_input in ['q', 'quit', 'Quit']:
            break

        if"set" in user_input:
            payload = user_input.split("set")[1]
            try:
                payload = payload.split(
                    ":") if":" in payload else payload.split("-")
                key = payload[0].strip()
                value = payload[1].strip()
                print(f"key:{key} || value: {value}")
                if s.set(key, value):
                    print("added to the store.")
            except:
                print("Ivalid syntax")

        elif"get" in user_input:
            key = user_input.split("get")[1].strip()

            value = s.get(key)
        if value:
            print(value)

        elif"save" in user_input:
            if s.save():
                print("saved")

        elif"clear" in user_input:
            if s.clear():
                print("cleared")

        elif"clear_snapshot" in user_input:
            if s.clear_snapshot():
                print("cleared")
