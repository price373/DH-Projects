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


def cut(args):  	    	       
    """remove sections from each line of files"""
    column = []
    if args[0] == "-f" and args[1].isdigit():
        column.append(args[1])
        filePaths = args[2:]
    elif args[0] == "-f" and not args[1].isdigit():
        column = args[1].split(sep=",")
        column.sort()
        filePaths = args[2:]
    elif args[0] == "-f":
        print(f"Invalid field value: {args[1]}")
        sys.exit(1)
    else:
        filePaths = args
        column.append(1)
    for filePath in filePaths:
        file = open(filePath)
        for line in file:
            displayValues = []
            for number in column:
                valueList = line.split(sep=",")
                if len(valueList) < int(column[-1]):
                    displayValues.append("")
                else:
                    displayValues.append(valueList[int(number)-1])
            joinStrings(displayValues)


def paste(args):
    """merge lines of files"""  	    	       
    fileList = []
    mostLines = 0
    for filePath in args:
        file = open(filePath)
        fileList.append(file)
        fileLines = file.readlines()
        if len(fileLines) > mostLines:
            mostLines = len(fileLines)
        file.seek(0)
    for num in range(mostLines):
        displayValues = []
        for currentFile in fileList:
            line = ""
            line = currentFile.readline()
            displayValues.append(line)
        joinStrings(displayValues)
    print()

def joinStrings(args):
    # Sub command for cut and paste to read list given and return a line separated by commas
    newLineList = []
    for line in args:
        newLine = line.split(sep="\n")
        newLineList.append(newLine[0])
    print(",".join(newLineList))