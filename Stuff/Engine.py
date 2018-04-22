import Model
import Serialize

# def work(): return [Animals.Model(item) for item in Serialize.Reader().deserialized]

def work():
    modellist = []
    for item in Serialize.Reader().deserialized:
        model = Model.Model(item)
        modellist.append(model)
    return modellist

