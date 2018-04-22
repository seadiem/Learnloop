import numpy

class Dataset:
    def __init__(self, json):
        self.targets = numpy.array(json["targets"])
        self.samples = numpy.array(json["samples"])
