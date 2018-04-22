import json
import ExampleClient
import Dataset

class DogClient:
    def __init__(self):
        self.socket = ExampleClient.Socket()
    def fetchTrainingset(self):
        answer = self.socket.send("trainingset")
        jsoner = json.loads(answer)
        data = Dataset.Dataset(jsoner)
        return data
    def fetchTestingset(self):
        answer = self.socket.send("testingset")
        jsoner = json.loads(answer)
        data = Dataset.Dataset(jsoner)
        return data
    def close(self):
        self.socket.close()


