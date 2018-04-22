from keras.models import Sequential
from keras.layers.core import Dense, Activation

def model():
    model = Sequential()
    model.add(Dense(16, input_shape=(4,)))
    model.add(Activation('sigmoid'))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    return model

def digit_model(inshape = (), outhape = 0 ):
    model = Sequential()
    model.add(Dense(16, input_shape=inshape))
    model.add(Activation('sigmoid'))
    model.add(Dense(outhape))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    return model