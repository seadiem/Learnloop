import numpy as np
import json
from Stuff import ExampleClient
import matplotlib.pyplot as plt

class Client:
    def __init__(self):
        self.socket = ExampleClient.Socket()
    def fetchDiagram(self):
        answer = self.socket.send("show")
        return answer
    def close(self):
        self.socket.close()

class Plotter:
    def __init__(self):
        c = Client()
        text = c.fetchDiagram()
        c.close()
        j = json.loads(text)
        self.array = np.array(j)
    def show(self):
        plt.imshow(self.array, cmap='gray', interpolation='none')
        plt.show(block = False)
