import numpy as np
from Stuff import ExampleServer
from Stuff import Dataset
import json
import Model
from Stuff import DogClient
from keras.utils import np_utils




class Predict:
    def __init__(self):
        client = DogClient.DogClient()
        data = client.fetchImages()
        client.close()
        self.uniques, self.ids = np.unique(data.targets, return_inverse=True)
        self.train_y_ohe = np_utils.to_categorical(self.ids)
        self.X_train = data.samples.reshape(data.samples.shape[0], data.samples.shape[1] * data.samples.shape[2])
        self.model = Model.digit_model(inshape = (self.X_train.shape[1],), outhape = self.uniques.shape[0])
    def fit(self,epochs = 0):
        self.model.fit(self.X_train, self.train_y_ohe, epochs=epochs, batch_size=1, verbose=1)
    def reload(self):
        self.model = Model.digit_model(inshape=(self.X_train.shape[1],), outhape=self.uniques.shape[0])
    def server(self):
        self.incom = ExampleServer.socketrun(loadfrom)
        return self.incom
    def predict(self):
        resX = self.incom.samples.reshape(1, self.incom.samples.shape[1] * self.incom.samples.shape[2])
        predict = self.model.predict_classes(resX)
        return self.uniques[predict]



def loadfrom(path):
    with open(path) as f:
        content = f.read()
    jsoner = json.loads(content)
    data = Dataset.Dataset(jsoner)
    return data

