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

class Card():  	    	       
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	    	       
    BINGO_BORDERS = "+-----"
    def __init__(self, idnum, num):
        """  	    	       
        Initialize a Bingo! card  	    	       
        """
        self.__m_idNum = idnum
        self.__m_num = num
        self.rows = []
        self.__borders = (self.BINGO_BORDERS * self.__m_num) + "+"

    def id(self):  	    	       
        """  	    	       
        Return an integer: the ID number of the card  	    	       
        """  	    	       
        return int(self.__m_idNum)

    def number_at(self, row, col):  	    	       
        """  	    	       
        Return an integer or a string: the value in the Bingo square at (row, col)  	    	       
        """  	    	       
        currentRow = self.rows[row]
        colNum = currentRow[col]
        return colNum
    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the length of one dimension of the card.  	    	       
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	    	       

        This method was called `size` in the C++ version  	    	       
        """  	    	       
        return self.__m_num

    def __str__(self):  	    	       
        """  	    	       
        Return a string: a neatly formatted, square bingo card  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """
        if not self.__m_num % 2 == 0:
            centerNum = (self.__m_num - 1) / 2
            midRow = self.rows[int(centerNum)]
            midRow[int(centerNum)] = -1
        cardString = f"Card #{self.__m_idNum}\n"
        for columns in range(self.__m_num):
            columnName = self.COLUMN_NAMES[columns]
            cardString += (f"{columnName:^6}")
        cardString += ("\n" + self.__borders + "\n")
        for rows in range(self.__m_num):
            currentRow = self.rows[rows]
            for cols in range(self.__m_num):
                columnData = currentRow[cols]
                if columnData == -1:
                    columnData = "Free!"
                cardString += (f"|{columnData:^5}")
            cardString += ("|\n" + self.__borders + "\n")
        return cardString
