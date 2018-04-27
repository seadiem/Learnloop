import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import json
from Stuff import Dataset
from Stuff import ExampleServer

class Digits:
    def __init__(self):
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_train = X_train.reshape(60000, 784)
        X_test = X_test.reshape(10000, 784)
        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')
        X_train /= 255
        X_test /= 255
        Y_train = np_utils.to_categorical(y_train, 10)
        Y_test = np_utils.to_categorical(y_test, 10)

        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        self.makemodel()

    def makemodel(self):
        model = Sequential()
        model.add(Dense(512, input_shape=(784,)))
        model.add(Activation('sigmoid'))
        model.add(Dense(10))
        model.add(Activation('softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
        self.model = model
        self.train()

    def train(self, epochs = 4, batchsize = 128):
        self.model.fit(self.X_train, self.Y_train, epochs = epochs, batch_size = batchsize, verbose = 1)

    def predict(self, array):
        array = array.reshape(1, 28, 28)
        array = array.reshape(1, 784)
        result = self.model.predict_classes(array)
        return result

class DogDigits():
    def __init__(self, shape = (28, 35)):
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_scale = self.reshapenp(X_train)
        x_scale = self.reshapenp(X_test)

        X_train = X_scale.reshape(60000, 28 * 35)
        X_test = x_scale.reshape(10000, 28 * 35)
        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')
        X_train /= 255
        X_test /= 255
        Y_train = np_utils.to_categorical(y_train, 10)
        Y_test = np_utils.to_categorical(y_test, 10)

        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        self.makemodel()

    def reshape(self, single):
        leftz = np.zeros((28, 3))
        rightz = np.zeros((28, 4))
        out = np.hstack((leftz, single, rightz))
        return out

    def reshapenp(self, array):
        l = []
        for item in array:
            out = self.reshape(item)
            l.append(out)
        out = np.array(l)
        return out

    def makemodel(self):
        model = Sequential()
        model.add(Dense(512, input_shape=(28 * 35,)))
        model.add(Activation('sigmoid'))
        model.add(Dense(10))
        model.add(Activation('softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
        self.model = model
        self.train()

    def train(self, epochs = 4, batchsize = 128):
        self.model.fit(self.X_train, self.Y_train, epochs = epochs, batch_size = batchsize, verbose = 1)

    def predict(self, array):
        array = array.reshape(1, 28, 35)
        array = array.reshape(1, 28 * 35)
        result = self.model.predict_classes(array)
        return result



class Server:
    def __init__(self): pass
    def server(self):
        self.incom = ExampleServer.socketrun(loadfrom)
        return self.incom

def loadfrom(path):
    with open(path) as f:
        content = f.read()
    jsoner = json.loads(content)
    data = Dataset.Dataset(jsoner)
    return data














