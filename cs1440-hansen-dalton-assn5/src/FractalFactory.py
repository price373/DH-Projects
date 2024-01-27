import Fractal
defaultFractal = {'centerx':     -0.363287878200906,'centery':     0.381197981824009, 'axislength':  0.0840187115019564,'type': 'phoenix', 'iterations': 256, 'pixels': 640, 'creal': 0.5667, 'cimag': 0, 'preal': -.5, 'pimag': 0}
def default():
    return defaultFractal
def makeFractal(fractalInfo):
    if fractalInfo == None:
        fractalInfo = default()
    fracType = fractalInfo['type']
    if fracType == 'phoenix':
        return Fractal.Phoenix(fractalInfo)
    elif fracType == 'mandelbrot':
        return Fractal.Mandelbrot(fractalInfo)
    elif fracType == 'spider':
        return Fractal.Spider(fractalInfo)
    elif fracType == 'mandelbrotcubed':
        return Fractal.MandelbrotCubed(fractalInfo)
    else:
        raise NotImplementedError("Unrecgonized Fractal Type ")
