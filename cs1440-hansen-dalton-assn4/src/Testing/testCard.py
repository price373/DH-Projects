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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class TestCard(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """  	    	       
        Create no fewer than 5 Card objects to test  	    	       

        Create a mixture of odd and even-sized cards  	    	       
        """  	    	       
        pass  	    	       


    def test_len(self):  	    	       
        """Assert that each card's size is as expected"""  	    	       
        pass  	    	       

    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""  	    	       
        pass  	    	       

    def test_freeSquares(self):  	    	       
        """  	    	       
        Ensure that odd-sized cards have 1 "Free!" square in the center  	    	       
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	    	       
        """  	    	       
        pass  	    	       

    def test_no_duplicates(self):  	    	       
        """Ensure that Cards do not contain duplicate numbers"""  	    	       
        pass  	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
