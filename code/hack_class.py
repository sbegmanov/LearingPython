
class Hack:
    numInstances = 0            # Use class method instead of static
    def __init__(self):
        Hack.numInstances += 1

    #@classmethod
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances)
    printNumInstances = classmethod(printNumInstances)
