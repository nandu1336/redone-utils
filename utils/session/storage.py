import os
from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass


class FileStorage(Storage):
    def __init__(self, folder=None, filename=None):
        self.folder = folder if folder else os.getcwd()
        self.filename = filename if filename else"session.txt"
        self.session = {}
        pass

    def open_file(self):
        session_file = os.path.join(self.folder, self.filename)
        fs = open(session_file, "w+")
        return fs

    def set(self, k, v):
        self.session[k] = v
        return True

    def get(self, k):
        if k in self.session.keys():
            return self.session[k]
        else:
            with open(os.path.join(self.folder, self.filename), "r") as f:
                lines = f.readlines()
            for line in lines:
                if line.split(":")[0] == k:
                    return line.split(":")[1]

            return""

    def save(self):
        with open(os.path.join(self.folder, self.filename), "a") as f:
            try:
                for key in self.session.keys():
                    f.writelines(f"{key}: {self.session[key]}\n")
                return True
            except:
                return False

    def clear(self, clear_snapshot=False):
        self.session = {}
        if clear_snapshot:
            with open(os.path.join(self.folder, self.filename), "w+") as f:
                f.truncate(0)


class RedisStorage(Storage):
    pass
