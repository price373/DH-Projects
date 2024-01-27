dictKeys = ['centerx','centery','axislength','type', 'iterations', 'pixels', 'creal', 'cimag', 'preal', 'pimag']

def parseFractalInfo(fracFile):
    file = open(fracFile)
    fracDict = {}
    for line in file:
        if line.isspace() or line[0] == '#' or line == '':
            continue
        else:
            line = line.strip()
            dataToAdd = line.split(":")
            if len(dataToAdd) > 2:
                continue
            if not dataToAdd[0].islower():
                dataToAdd[0].lower()

            value = dataToAdd[1].strip()
            fracDict[dataToAdd[0]] = value
    verifyFractalInfo(fracDict)
    return fracDict
def verifyFractalInfo(fractalDict):
    fractalDict = {}
    for key in dictKeys:


        if (key == 'creal' or key == 'cimag' or key == 'preal' or key == 'pimag') and not fractalDict.__contains__(key):
            continue
        elif key in fractalDict:
            raise RuntimeError (f"required information {key} is missing from file.")
        elif fractalDict.get(key):
            continue

