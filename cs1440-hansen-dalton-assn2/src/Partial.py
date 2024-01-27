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


def head(args):  	    	       
    """output the first part of files"""  	    	       
    if args[0] == "-n" and args[1].isdigit():
        N = args[1]
        filePaths = args[2:]
    elif args[0] == "-n":
        N = 10
        filePaths = args[1:]
    else:
        N=10
        filePaths = args
    for filePath in filePaths:
        if len(filePaths) > 1:
            print(f"==> {filePath}")
        file = open(filePath)
        fileLines = file.readlines()
        for num in range(int(N)):
            print(fileLines[num],end ="")
        file.close()
        print()

def tail(args):  	    	       
    """output the last part of files"""
    if args[0] == "-n" and args[1].isdigit():
        N = args[1]
        filePaths = args[2:]
    elif args[0] == "-n"and not args[1].isdigit():
        print("INVALID LINE NUMBERS: defaulting to 10")
        N = 1-0
        filePaths = args[1:]
    else:
        N = 10
        filePaths = args
    for filePath in filePaths:
        file = open(filePath)
        fileLines = file.readlines()

        for num in range(int(N)):
            print(fileLines[num],end="")
        file.close()
    print()
