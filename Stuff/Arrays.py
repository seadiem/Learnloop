import numpy

def f(x, y):
    return  10*x+y

def make():
    return numpy.fromfunction(f, (5,4))
