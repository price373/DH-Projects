#!/usr/bin/env python3  	    	       


#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       

import unittest  	    	       
import PaletteFactory
from Fractal import Mandelbrot
from Fractal import Phoenix
# autocmd BufWritePost <buffer> !python3 runTests.py

class TestPaletteFactory(unittest.TestCase):

    def test_colorOfThePixel(self):
        iters = {'iterations': '256'}
        mandelbrot = Mandelbrot(iters)
        cold = PaletteFactory.makePalette(iters, 'coldPalette')
        self.assertEqual(cold.getColor(mandelbrot.count(complex(0, 0))), '#9c44f3')
        self.assertEqual(cold.getColor(mandelbrot.count(complex(-0.751, 1.1075))), '#9c44f3')
        self.assertEqual(cold.getColor(mandelbrot.count(complex(-0.2, 1.1075))), '#ee82ee')
        self.assertEqual(cold.getColor(mandelbrot.count(complex(-0.75, 0.1075))), '#9c44f3')
        self.assertEqual(cold.getColor(mandelbrot.count(complex(-0.748, 0.1075))), '#9c44f3')


    def test_palleteLength(self):
        iters = {'iterations': '256'}
        cold = PaletteFactory.makePalette(iters, 'coldPalette')
        self.assertEqual(cold.__getListLength__(), 3)
        royalPalette = PaletteFactory.makePalette(iters, 'royalPalette')
        self.assertEqual(royalPalette.__getListLength__(), 256)
if __name__ == '__main__':
    unittest.main()

