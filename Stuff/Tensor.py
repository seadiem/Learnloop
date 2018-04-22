from __future__ import absolute_import, division, print_function
import tensorflow as tf
import tensorflow.contrib.eager as tfe

def parse_csv(line):
  example_defaults = [[0.], [0.], [0.], [0.], [0]]  # sets field types
  parsed_line = tf.decode_csv(line, example_defaults)
  # First 4 fields are features, combine into single tensor
  features = tf.reshape(parsed_line[:-1], shape=(4,))
  # Last field is the label
  label = tf.reshape(parsed_line[-1], shape=())
  return features, label

class Model:
    def getmodel(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation="relu", input_shape=(4,)),  # input shape required
            tf.keras.layers.Dense(10, activation="relu"),
            tf.keras.layers.Dense(3)
        ])
        return model

def loss(model, x, y):
  y_ = model(x)
  return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)

def grad(model, inputs, targets):
  with tfe.GradientTape() as tape:
    loss_value = loss(model, inputs, targets)
  return tape.gradient(loss_value, model.variables)


def getoptimizer():
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    return optimizer

class Optimizer:
    def getoptimizer(self):
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
        return optimizer
