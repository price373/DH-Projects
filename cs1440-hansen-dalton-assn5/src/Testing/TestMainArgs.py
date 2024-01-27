import unittest
import FractalParser
class TestArgs(unittest.TestCase):
    def test_processArgs(self):
        args1 = ['src/main.py', 'data/mandelbrot.frac']
        self.assertEqual(FractalParser.parseFractalInfo(args1[1])['type'], 'mandelbrot')
        args2 = ['src/main.py', 'data/mandabot.frac']
        try:
            FractalParser.parseFractalInfo(args2[1])
        except FileNotFoundError:
            a = True
        finally:
            self.assertTrue(a)

