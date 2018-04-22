import os
import json


class Pathmaker:
    def __init__(self):
        self.path = self.getPath()
    def getPath(self): return os.environ["LEARNSHARED"]
    def getFilePath(self): return self.path + "/file.json"


class Reader:
    def __init__(self):
        with open(Pathmaker().getFilePath()) as f:
            content = f.read()
        content = content.rstrip(',')  # remove the last comma
        content = '[' + content + ']'
        self.deserialized = json.loads(content)

class ObjectReader:
    def __init__(self):
        with open(Pathmaker().getFilePath()) as f: content = f.read()
        self.deserialized = json.loads(content)

# for * splitter

class Loader:
    def __init__(self):
        self.split = self.load()

    def load(self):
        path = Pathmaker().getFilePath()
        s = open(path)
        data = s.read()
        split = data.split("*")
        return split


class Serializer:
    def __init__(self):
        splits = Loader().split
        dump = json.dumps(splits)
        load = json.loads(dump)
        ready = []
        for item in load:
            if len(item) > 0:
                j = json.loads(item)
                ready.append(json)
        self.ready = ready
