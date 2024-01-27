#!/usr/bin/python3  	    	       

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


# python -m pip install --user -r requirements.txt  	    	       
from bs4 import BeautifulSoup  	    	       
from urllib.parse import urlparse, urljoin, urldefrag  	    	       
import requests
import sys  	    	       
import time  	    	       

def validateURL(url):
    parsedURL = urlparse(url)
    # checks the pieces to verify what it is and sends back a code for future use.
    if parsedURL.scheme == 'http' or parsedURL.scheme == 'https':
        return 1
    elif parsedURL.path and not parsedURL.scheme:
        return 2
    else:
        return 0

def crawl(url, maxDepth, visitedURLs=set()):
    #Creates defaults and basic use cases for recursive function

    if validateURL(url) != 1:
        print("Invalid URL: Please ensure an Absolute URL or url with 'http://' or 'https://' scheme is used")
        sys.exit(1)
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
    startTime = time.time()
    try:
        recursiveCrawl(url, 0, maxDepth, visitedURLs)
    except KeyboardInterrupt:
        print("Process Terminated: User Exit")
    finally:
        endTime = time.time() - startTime
        print(f'Visited {len(visitedURLs)} unique sites in {endTime} seconds.')

def recursiveCrawl(url, recursionDepth, maxDepth, visitedURLs):
    """  	    	       
    Given an absolute URL, print each hyperlink found within the document.  	    	       
    This function will need more parameters.  	    	       

    Your task is to make this into a recursive function that follows hyperlinks  	    	       
    until one of two base cases are reached:  	    	       

    0) No new, unvisited links are found  	    	       
    1) The maximum depth of recursion is reached  	    	       
    """
    if recursionDepth > maxDepth:
        return
    if url in visitedURLs:
        return
    if validateURL(url) == 0:
        return
    print("    " * recursionDepth + url)
    visitedURLs.add(url)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for a in links:
            href = a.get('href')
            if not href:
                continue
            href = urldefrag(href).url
            if validateURL(href) == 2:
                newUrl = urljoin(url, href)
            else:
                newUrl = href
            recursiveCrawl(newUrl, recursionDepth+1, maxDepth, visitedURLs)
    except Exception as e:
        print(f'Error: {e}')



# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	    	       
if __name__ == "__main__":  	    	       

    ## If no arguments are given...  	    	       
    if len(sys.argv) < 2:  	    	       
        print("Not enough Arguments given: Please Input an Absolute URL starting with 'https' or 'http'. Recursion depth argument Optional\n For more info please refer to the User Manual")
        exit(0)  	    	       
    elif len(sys.argv) >= 3:
        url = sys.argv[1]
        maximumDepth = sys.argv[2]
        if not maximumDepth.isnumeric():
            maximumDepth = None
    else:
        maximumDepth = 3
        url = sys.argv[1]

    crawl(url, int(maximumDepth))
