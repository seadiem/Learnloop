import os
import sys

def parseline(line=""):
    name = line[:31]
    number = line[0 + 32 + 40: 0 + 32 + 40 + 10]
    number.replace(" ", "")
    try:
        i = int(number)
        return (name, int(number))
    except:
        raise



def pars(path=""):
    with open(path) as f:



        for line in f:
            try:
                out = parseline(line)
                print  "name: {} count: {}".format(out[0], out[1])
            except:
                pass






def main():
    script = sys.argv[0]
    filepath = sys.argv[1]
    pars(filepath)


main()