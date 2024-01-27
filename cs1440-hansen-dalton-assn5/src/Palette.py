import colour

class Palette:

    def __init__(self, iterations):
        self.numColors = iterations
        self.colorList = []
    def getColor(self,num):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
    def __getListLength__(self):
        return len(self.colorList)
class dynamicPalette(Palette):
    def __init__(self, iterations):
        red = colour.Color('red')
        green = colour.Color('green')
        self.colorList = list(red.range_to(green, iterations))
    def getColor(self,num):
        return self.colorList[num].get_hex_l()
class coldPalette(Palette):
    def __init__(self, iterations):
        blue = colour.Color('blue')
        violet = colour.Color('violet')
        self.colorList = list(blue.range_to(violet, 3))
    def getColor(self,num):
        if num % 2 == 0:
            return self.colorList[1].get_hex_l()
        elif num % 3 == 0:
            return self.colorList[2].get_hex_l()
        else:
            return self.colorList[0].get_hex_l()


class royalPalette(Palette):
    def __init__(self, iterations):
        yellow = colour.Color('yellow')
        violet = colour.Color('violet')
        self.colorList = list(yellow.range_to(violet, int(iterations)))
    def getColor(self,num):
        return self.colorList[num-1].get_hex_l()




