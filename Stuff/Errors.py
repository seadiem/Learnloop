class ColorError(Exception):
    def __init__(self, type=2):
        self.type = type


class Error(Exception):
    def __init__(self):
        self.msg = "error"

class SwiftError(Exception):
    def __init__(self, msg):
        self.msg = "swift error:" + " " + msg

class ShapeError(Exception):
    pass

class TypeError(Exception):
    pass

class Work:
    def __init__(self, number):
        if number > 10: raise Error()
        else: self.number = number

def first(n):
    try:
        w = Work(n)
    except:
        print("some error")