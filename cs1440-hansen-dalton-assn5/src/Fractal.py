class Fractal:
    maxIterations = 0
    def __init__(self, fractalInfo):
        self.fractalInfo = fractalInfo
        self.maxIterations = int(fractalInfo['iterations'])
    def count(self, compCoords):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
class Mandelbrot(Fractal):
    def count(self, compCoords):
        z = complex(0, 0)
        for iteration in range(self.maxIterations):
            z = z * z + compCoords
            if abs(z) > 2:
                return iteration
        return self.maxIterations
class MandelbrotCubed(Fractal):
    def count(self, compCoords):
        z = complex(0, 0)
        for iteration in range(self.maxIterations):
            z = z^[3] + compCoords
            if abs(z) > 2:
                return iteration
        return self.maxIterations
class Phoenix(Fractal):
    def count(self, compCoords):
        coordsFlipped = complex(compCoords.imag, compCoords.real)
        prevCompCoords = complex(0, 0)
        c = complex(self.fractalInfo['creal'], self.fractalInfo['cimag'])
        z = complex(self.fractalInfo['preal'], self.fractalInfo['pimag'])
        for iteration in range(self.maxIterations):
            savedCoords = coordsFlipped
            coordsFlipped = coordsFlipped * coordsFlipped + c + (z * prevCompCoords)
            prevCompCoords = savedCoords
            if abs(coordsFlipped) > 2:
                return iteration
        return self.maxIterations
class Spider(Fractal):
    def count(self, compCoords):
        z = complex(0, 0)
        c = compCoords
        for iteration in range(self.maxIterations):
            z = z * z + c
            c = c/2 + z
            if abs(z) > 2:
                return iteration
        return self.maxIterations









