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
    def fetchImages(self):
        path = self.socket.send("dataset")
        with open(path) as f:
            content = f.read()
        jsoner = json.loads(content)
        data = Dataset.Dataset(jsoner)
        return data
    def close(self):
        self.socket.close()


