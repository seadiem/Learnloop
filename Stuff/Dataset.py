import numpy
import json

class Dataset:
    def __init__(self, json):
        self.targets = numpy.array(json["targets"])
        self.samples = numpy.array(json["samples"])

def loadfrom(path):
    with open(path) as f:
        content = f.read()
    jsoner = json.loads(content)
    data = Dataset(jsoner)
    return data

