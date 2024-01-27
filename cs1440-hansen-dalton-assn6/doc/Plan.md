# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

* Use recursion and modules to create a web crawler application to find urls and link on html pages. So using Beautiful soup to inspect the HTML and
requests to get URLs while parsing the URLs to identify looping.
    * This program is aiming to provide a way to find all of the links and crawl across the internet.
    * So a good solution will have some small functions to help parse and change aspects of the URLS however most of the work will be done by the recursive crawl() function
    * I already know a little bit of how URLs and recursive functions work now
    * I Might struggle using the Libraries however.

## Phase 1: System Analysis *(10%)*
Some data used by these functions are initial URL, accessing the URL webpage and then finding URLs on the original.
* The output will mostly be a group of reports on visited urls as well as number of unique pages and time.
* Algrithms like recursion, head or tail, and argument processing will be used to both receive and interpret URLs and input
data.

## Phase 2: Design *(30%)*
#### crawl: function called to begin recursion
``` 
crawl(url: string, maxDepth: int(default = 3), visitedURls: set (default = empty set):
    # Creates defaults and basic use cases for recursive function
    check validity of given URl (use validateURL
    if maxDepth < 1 or maxDepth not numeric:
        maxDepth = 3
    print starting url and maxDepth
    start time
    try:
        recursiveCrawl(url,depth = 0, maxDepth, visitedURLs)
    catch keyboardInterrupt:
        print ended by user message
    finally:
        end time is equal to time - start time
        'visited "visitedURL length" unique sites in "end time" seconds
```
good input: receives input and begins recursive function, exits when keyboard interrupt used
bad input: fixes faulty info or exits if there is an incorrect url.
#### recursiveCrawl: receives url and recursively searches through the program
```
recursiveCrawl(url: string, recursionDepth: int,maxDepth: int, visitedURLs : set):
    if the current recursionDepth is greater than the maxDepth:
        return
    if URL has already been visted:
        return
    if URL is invalid:
        return
    print out URL with added indentation based on recursionDepth
    add URL to visitedURLs.
    # handle exceptions
    try:
        Get Page using 'requests' library
        Use beautifulsoup to find all URL links and place them into list
        don't just print URLs, dive into them
        for each <a> tag:
          check if href attribute is present
          if not:
            continue
          trim fragments
          if not absolute URL: 
            make absolute address (only HTTP or HTTPS) {use urljoin}
          recursiveCrawl(newURL: string, recursionDepth + 1, maxDepth, visitedURLs
    catch Exception:
        print out Error message 
```
good input: No errors will occur and the program will print all valid links, up to how deep user want to go, then print all URLs using incrementation to show depth.
bad input: Error message will occur, as there is not proper input, otherwise Not many will be placed.
#### validateURL: check if given URL is valid
```
validate_URL(url:string):  
    parsedURL = urlparse(url)
    # checks the pieces to verify what it is and sends back a code for future use.
    if scheme of parsedURL is 'http' or 'https':
        return 1
    if not scheme and is path:
        return 2
    else:
        return 0 
```
## Phase 3: Implementation *(15%)*
Everthing went according to plan except my plan to remove fragments and my implementation of the response, as there are several ways to keep them out
## Phase 4: Testing & Debugging *(30%)*

ran the test server with parameter timer =0 and using default depths and overidden depth of 4 to properly find how the program processes
these urls and puts them into tree-like indentations.

## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance

*   Fill out the Assignment Reflection on Canvas.
Honestly I don't think I wrote sloppy code, however I think I could have done better
* and I do not have enough documentation in all honesty, its something I really struggle with,
* It should be really easy to add new features, as I also implemented a url validator, to help modularize the functions.
* I think this program should still function for a long time as things update and upgrade.