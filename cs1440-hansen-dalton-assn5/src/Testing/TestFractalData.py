import unittest
import FractalParser
import FractalFactory
class TestFractalInformation(unittest.TestCase):
    def test_FractalDicts(self):
        self.assertEqual(FractalParser.parseFractalInfo('data/mandelbrot-zoomed.frac'), {'type': 'mandelbrot', 'pixels': '640', 'centerx': '-1.0', 'centery': '0.0', 'axislength': '1.0','iterations': '256'})
        self.assertEqual(FractalParser.parseFractalInfo('data/phoenix.frac'),  {'type': 'phoenix', 'preal': '-0.5', 'pimag': '0.0', 'creal': '0.5667', 'cimag': '0.0', 'centerx': '0', 'centery': '0', 'axislength': '3.25', 'pixels': '512', 'iterations': '101'})

    def test_FractalData(self):
        mandelbrot = FractalParser.parseFractalInfo("data/mandelbrot.frac")
        self.assertEqual(mandelbrot['centerx'], '0.0')
        self.assertEqual(mandelbrot['centery'], '0.0')
        self.assertEqual(mandelbrot['axislength'], '4.0')
        self.assertEqual(mandelbrot['type'], 'mandelbrot')
        self.assertEqual(mandelbrot['iterations'], '100')
        self.assertEqual(mandelbrot['pixels'], '640')
        phoenix = FractalParser.parseFractalInfo("data/phoenix.frac")
        self.assertEqual(phoenix['centerx'], '0')
        self.assertEqual(phoenix['centery'], '0')
        self.assertEqual(phoenix['axislength'], '3.25')
        self.assertEqual(phoenix['type'], 'phoenix')
        self.assertEqual(phoenix['pixels'], '512')
        self.assertEqual(phoenix['iterations'], '101')
        self.assertEqual(phoenix['creal'], '0.5667')
        self.assertEqual(phoenix['cimag'], '0.0')
        self.assertEqual(phoenix['preal'], '-0.5')
        self.assertEqual(phoenix['pimag'], '0.0')
