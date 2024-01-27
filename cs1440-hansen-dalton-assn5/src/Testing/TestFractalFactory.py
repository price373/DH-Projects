import unittest
import FractalFactory
from Fractal import Mandelbrot

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestFractalFactory(unittest.TestCase):
    def testFractalCreation(self):
        mandel = Mandelbrot({'iterations': '512'})
        factDict = {'type': 'mandelbrot', 'iterations': '512'}
        factMandel = FractalFactory.makeFractal(factDict)
        self.assertEqual(mandel.count(complex(0,0)),factMandel.count(complex(0,0)))
    def testDefault(self):
        peacock = {'centerx': -0.363287878200906, 'centery': 0.381197981824009, 'axislength': 0.0840187115019564,'type': 'phoenix', 'iterations': 256, 'pixels': 640, 'creal': 0.5667, 'cimag': 0,'preal': -.5, 'pimag': 0}
        peacockFrac = FractalFactory.makeFractal(peacock)
        factDefault = FractalFactory.makeFractal(None)
        self.assertEqual(peacockFrac.count(complex(0,0)), factDefault.count(complex(0,0)))