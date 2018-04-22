import os
import subprocess
import json
import numpy
import Errors

class SwiftStarter:
    """
    data = SwiftStarter.SwiftStarter(["one", "two"]).data
    """
    def __init__(self, c = []):
        c = os.environ["DOG"]
        self.command = "swift run --package-path" + " " + c + " TestLearn"
        result = self.run(c)
        self.data = Numpy(result)

    def run(self, c = []):
        args = ""
        for item in c:
            args += " "
            args += item
        finalcommand = self.command + args
        result = subprocess.check_output(finalcommand, shell=True)

        try:
            parser = Parser(result)
            jsoner = Json(parser.clear)
            return jsoner.jsonobject
        except Errors.SwiftError as error:
            print error.msg
            raise
        except:
            print "Undefined error, from swift" + " " + parser.clear
            raise


class Parser:
    def __init__(self, s):
        try:
            clear = s[s.index("*") + 1:s[s.index("*") + 1:].index("*") + s.index("*") + 1] # or regex
            self.clear = clear
        except:
            error = Errors.SwiftError(s)
            raise error


class Json:
    def __init__(self, l):
        self.jsonobject = json.loads(l)

class Numpy:
    def __init__(self, json):
        self.targets = numpy.array(json["targets"])
        self.samples = numpy.array(json["samples"])
