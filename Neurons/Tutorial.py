import numpy as np

def shapeThreeToTwo(n=np.array([1])):
    l = n.shape[0]
    numbers = n.shape[1] * n.shape[2]
    finalshape = (l, numbers)
    return finalshape

def reshapeThreeToTwo(n=np.array([1])):
    outershape = shapeThreeToTwo(n)
    out = n.reshape(outershape)
    return out

