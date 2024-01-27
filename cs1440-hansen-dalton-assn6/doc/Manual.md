# Recursive Web Crawler User Manual
## Setup
To set up your python, run this command:
```commandline
python.exe -m pip install --user -r requirements.txt
```
This will download all required packages used in the web crawler.
## How to Run crawler.py 
* Verify you are in the main directory (for this program the cs1440-hansen-dalton-assn6 directory)
* The program takes URL or URL and a maximum recursion depth as arguments:
  * URLs are required and are simply a common web URL
    * Absolute URLs are what is used, an absolute url is a url with 'http://' or 'https://' at the beginning of the url
    * Relative urls do not have this piece of information and cannot be used as arguments in the program.
  * Maximum Recursion Depth refers to the number of times the program will read pages from the first page
    * So if  the maximum recursion depth is 5 it will open the starting url, find all the links and open them, and continue until this happens 5 times.
  * The Maximum Recursion depth parameter is optional, but the URL is not.
```commandline
/cs1440-hansen-dalton-assn6$ python.exe src/crawler.py https:/unnovative.net/levels/level1.html
```
### OR
```commandline
/cs1440-hansen-dalton-assn6$ python.exe src/crawler.py https:/unnovative.net/levels/level1.html 5
```
## What you should see
1. The starting URL and depth of recursion
1. List of all visited URLs with indentation of how deep they are in the recursion.
1. Number of Unique Pages visited and the time it took to visit all of them
   * It is possible to also see a user interruption message if the user used the Keyboard Interrupt command.
### Possible Errors
* Relative URL instead of absolute URL:
  * Absolute: 'http://unnovative.net/levels/level1.html'
  * Relative: 'unnovative.net/levels/level1.html'
* No arguments after program call
* Only maximum recursive depth is given as argument.