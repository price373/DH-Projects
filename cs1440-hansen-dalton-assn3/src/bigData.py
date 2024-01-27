#!/usr/bin/env python  	    	       

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
# The above copyright notice and this permission notice shsoft be included in
# soft copies or substantial portions of the Software.
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


import time  	    	       
import sys  	    	       
from Report import Report  	    	       


rpt = Report(year=2021)  	    	       
def readAreaTitles(directory):
    includedFips = {}
    fileDirectory = (directory + "/area-titles.csv")
    areaFile = open(fileDirectory)
    for line in areaFile:
        currentLine = line.split(sep=",", maxsplit=1)
        currentLineFips = currentLine[0]
        if currentLineFips[1].isdigit(): # and not currentLineFips.endswith("000"):
            if not currentLineFips.endswith('000"'):
                includedFips[currentLineFips] = currentLine[1].removesuffix('\n').strip('"')
            else:
                continue
        else:
            continue
    return includedFips


def readAnnualSingleFile(directory, includedFips):
    fileDirectory = (directory + "/2021.annual.singlefile.csv")
    annualFile = open(fileDirectory)
    for line in annualFile:
        currentLine = line.split(sep=",")
        currentFips = currentLine[0]

        if includedFips.__contains__(currentFips):
            if currentLine[1] == '"0"' and  currentLine[2] == '"10"':
                rpt.all.total_annual_wages += int(currentLine[10])
                if int(currentLine[10]) > rpt.all.max_annual_wage[1]:
                    rpt.all.max_annual_wage[0] = includedFips[currentFips]
                    rpt.all.max_annual_wage[1] = int(currentLine[10])
                rpt.all.total_empl += int(currentLine[9])
                if int(currentLine[9]) > rpt.all.max_empl[1]:
                    rpt.all.max_empl[0] = includedFips[currentFips]
                    rpt.all.max_empl[1] = int(currentLine[9])
                rpt.all.total_estab += int(currentLine[8])
                if int(currentLine[8]) > rpt.all.max_estab[1]:
                    rpt.all.max_estab[0] = includedFips[currentFips]
                    rpt.all.max_estab[1] = int(currentLine[8])
                rpt.all.num_areas += 1
            elif currentLine[1] == '"5"' and currentLine[2] == '"5112"':
                rpt.soft.total_annual_wages += int(currentLine[10])
                if int(currentLine[10]) > rpt.soft.max_annual_wage[1]:
                    rpt.soft.max_annual_wage[0] = includedFips[currentFips]
                    rpt.soft.max_annual_wage[1] = int(currentLine[10])
                rpt.soft.total_empl += int(currentLine[9])
                if int(currentLine[9]) > rpt.soft.max_empl[1]:
                    rpt.soft.max_empl[0] = includedFips[currentFips]
                    rpt.soft.max_empl[1] = int(currentLine[9])
                rpt.soft.total_estab += int(currentLine[8])
                if int(currentLine[8]) > rpt.soft.max_estab[1]:
                    rpt.soft.max_estab[0] = includedFips[currentFips]
                    rpt.soft.max_estab[1] = int(currentLine[8])
                rpt.soft.num_areas += 1
            else:
                continue
        else:
            continue
if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Argument Error: bigData.py takes exactly [1] Argument")
        print("Usage: bigData.py FILE_DIRECTORY")
        sys.exit(1)
    print("Reading the databases...", file=sys.stderr)  	    	       
    before = time.time()
    includedAreas = readAreaTitles(sys.argv[1])
    readAnnualSingleFile(sys.argv[1], includedAreas)
    after = time.time()  	    	       
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    # Print the completed report  	    	       
    print(rpt)  	    	       

