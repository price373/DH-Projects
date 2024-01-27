import Palette
def defaultPalette():
    return 'coldPalette'
def makePalette(fractalInfo, paletteName):
    iterations = int(fractalInfo['iterations'])
    if paletteName == 'coldPalette':
        return Palette.coldPalette(iterations)
    elif paletteName == 'dynamicPalette':
        return Palette.dynamicPalette(iterations)
    elif paletteName == 'royalPalette':
        return Palette.royalPalette(iterations)
    else:
        raise NotImplementedError ("Unrecognized  PaletteName")