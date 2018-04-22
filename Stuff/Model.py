import Errors

class Library:
    def __init__(self, attributes):
        self.label = attributes["labels"]
        self.features = attributes["features"]

class Model:
    def __init__(self, attributes):
        self.label = Label(attributes["label"])
        self.features = Features(attributes["features"])


class Features:
    def __init__(self, attributes):
        self.phisics = Phisics(attributes["phisics"])
        self.biology = Biology(attributes["biology"])


# Phisics
class Phisics:
    def __init__(self, attributes):
        self.move = Move(attributes["move"])
        self.size = Size(attributes["size"])

class Size:
    def __init__(self, attributes):
        self.width = attributes["widht"]
        self.height = attributes["height"]
        self.weight = attributes["weight"]

class Move:
    def __init__(self, attributes):
        self.accelrate = attributes["accelrate"]


#Biology
class Biology:
    def __init__(self, attributes):
        try: color = Color(attributes["color"])
        except: raise Errors.ColorError()
        else: self.color = color

class Color:
    def __init__(self, color):
        self.color = color
        if self.color == "Red": self.id = 0
        if self.color == "Orange": self.id = 1
        if self.color == "Yellow": self.id = 2
        if self.color == "Green": self.id = 3
        if self.color == "Cyan": self.id = 4
        if self.color == "Blue": self.id = 5
        if self.color == "Violette": self.id = 6
        try: range(7).index(self.id)
        except: raise Errors.ColorError()



# Label
class Label:
    def __init__(self, attributes):
        self.name = attributes["name"]







# Number appearence
class ModelNumber:
    def __init__(self, model):
        pass




