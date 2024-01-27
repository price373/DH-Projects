# CS 1440 Assignment 6: Recursive Web Crawler - Instructions

[TOC]


## Description

Use 3rd-party libraries to quickly produce a functioning web crawler.  Rely on
Exception Handling to deliver a safe and robust solution to our client.
Deliver a well-tested and documented programming product by the end of the
sprint.


## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 5.2
Average Score % (Grade)          | 79.3% (C+)
% students thought this was Easy | 56.8%
... Medium                       | 29.5%
... Hard                         | 1.1%
... Too Hard/Did not complete    | 11.6%


## Project Requirements (85 points in total)

*   **IMPORTANT: This assignment is *not* eligible for the grading gift.  This due date cannot be moved**
0.  **Late Penalty**:
    *   \<24hrs late = Score is capped at 75% of total
    *   \>=24hrs & <48hrs = Score is capped at 50% of total
    *   \>=48hours = submissions are not allowed
1.  **100% penalty** if your program imports any modules **except**:
    *   `sys`
    *   `time`
    *   `typing`
    *   `requests`
    *   `bs4`, specifically `BeautifulSoup`
    *   `urllib.parse`, specifically `urlparse` and `urljoin`
    *   modules you wrote yourself
2. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
3. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration
4. **10 point penalty** `eval()` or a similar function is used by your program
    *   use type constructor functions such as `int()` and `float()` instead


### SDP and DuckieCorp Conventions (25 points)

0.  Tag `analyzed` on the commit at the end of **Phase 1: System Analysis**.  Your work up to this point includes:
    *   Carefully study the [Requirements](#requirements) section below
    *   `Plan.md`: Phases 0 and 1 are complete
    *   `Signature.md` is updated with your activity up to this point
    *   *Grace Points* if this tag is pushed by end of day on **Sunday, the 4th of December**, you will receive up to 5 points back from other lost points on this assignment
1.  Tag `designed` on the commit at the end of **Phase 2: Design**.  Your work up to this point includes:
    *   A draft of the **User's Manual** describing the anticipated user interface (UI) of the final product
    *   `Plan.md`: Phase 2 includes **clear and easy to read** descriptions and pseudocode for each function/method that you will write in the program (you are not required to write pseudocode for code provided by the instructor).
        *   Filler text is **erased** once your information is filled in
        *   Do not paste Python code into the Plan document
        *   Try not to write executable pseudocode; *if we can paste your pseudocode into the REPL and run it, you're doing it wrong*
    *   `Signature.md` is updated
    *   *Grace Points* if this tag is pushed by end of day on **Sunday, the 4th of December**, you will receive up to 5 points back from other lost points on this assignment
2.  Tag `implemented` on the commit at the end of **Phase 3: Implementation**.  Your work up to this point includes:
    *   Runnable source code under `src/`
    *   `Plan.md`: Phase 3 is written and **does NOT** include code copied from your program
        *   Changes from your original plan are noted here, with an explanation of why it changed
        *   If you did not deviate from your plan, erase the filler text and leave this phase blank
    *   `Signature.md` is updated
3.  Tag `tested` on the commit at the end of **Phase 4: Testing and Debugging**.
    *   It is your responsibility to ensure that your program will work on your grader's computer
        *   Code that crashes and cannot be quickly & easily fixed by the grader will receive 0 points on the relevant portions of the rubric
        *   Code that crashes and CAN be quickly & easily fixed by the grader (or crashes only part of the time) will receive, at most, half-credit on the relevant portions of the rubric
    *   *This tag may be on the same commit as `implemented`*.  Your work up to this point includes:
    *   `Plan.md`: Phase 4 lists the *commands* you ran to test your program, with brief descriptions of what a user should expect to see when they run the same commands.
            * Example:
                ```
                Command: <what command did you run in the command line>
                Bug Found: <if a bug was found, what was it? Otherwise note here that it worked as expected>
                Bug Fixed: <if there was a bug, then note here how you fixed it>
                ```
        *   This proves that you tested your program, and helps us to replicate your results.
        *   It also tells us what bugs were found and how you fixed them.
        *   Filler text is **erased** once your information is filled in.
    *   `Signature.md` is updated.
4.  Tag `deployed` on the commit that you want us to grade for this sprint.
    *   *This tag may be on the same commit as `tested` and `implemented`*.  Your work up to this point includes:
    *   `Plan.md`
        *   Phase 5 may be left blank, there isn't much for you to say.
        *   Phase 6 is filled out, organized and easy-to-read.
        *   Filler text is **erased** once your information is filled in.
    *   `Signature.md` is filled out
        *   The *TODO* and *Nocember* placeholder entries are removed from the final draft
        *   The **TOTAL** line is present and agrees with your daily entries (*exception:* you don't need a separate **TOTAL** line if you worked on the project for only one day)
    *   **OPTIONAL** If you have special instructions for the grader, *erase the contents of `README.md` in the root directory* and replace it with your instructions.
5.  Push all tags **and** the `master` branch to GitLab before the due date
    *   Mind the capitalization and spelling of tags!
    *   Run these commands in the deployed phase to turn in all of your work:
        *   `$ git push origin master`
        *   `$ git push origin --tags`


#### Penalties

0.  **10 point penalty** your repository's URL on GitLab does not follow the naming convention
1.  **10 point penalty** your project is not a clone of the starter code repository
2.  **10 point penalty** there is an omission of required files and directories (missing, renamed, or moved from their expected location)
3.  **10 point penalty** there is no `.gitignore` (either missing or corrupted)
4.  **10 point penalty** there are forbidden files and directories in the submission
5.  **0.5 point penalty** per tag that is misspelled


### User's Manual (10 points)

*   A **first draft** written at or before the `designed` commit
    *   Describe your *expectation* of how the program will work, from the user's perspective
    *   If the first draft of the manual is not present, you will receive *at most* half credit
*   A **final draft** written at or before the `deployed` commit
    *   Describe how your program *actually* works

Write your instructions with the end-user in mind; your audience is not a programmer.
You may assume the user can use the command line and knows how to run Python and pip on their computer.
A good manual does not need to be long, but covers these points:

*   **Setup steps** the user must complete before they can use the program
    *   You may simply tell the user to run `python -m pip install --user -r requirements.txt`
*   Explain **how to run** the program
    *   What is the name of the program?
    *   Which directory should the user start in?
    *   What arguments does the program take?
        *   Explain the difference between *absolute* and *relative* URLs
        *   Explain what effect the maximum recursion depth has
        *   Which arguments are optional, and what is the default behavior when they are not specified?
*   Describe what the user sees when the **program runs correctly**
*   Show **common errors** when the program is used incorrectly
    *   Contrast valid and invalid inputs


### User Interface: Input (10 points)

*   When **zero** command line arguments are given:
    *   Display a *simple* usage message explaining what arguments can be given to the program and immediately exit
*   When **one** command line argument is given
    *   The first argument is the `StartingURL` that your `crawl()` function will visit first
        *   `StartingURL` must be an *absolute URL* that begins with either `http://` or `https://`
    *   Print an error message to `sys.stderr` and quit when this URL is not *absolute*, or does not begin with `http://` or `https://`
        *   This must be your own error message; it is wrong if the `requests` library raises an exception
        *   You do not need a `try/except` block to accomplish this; instead, inspect the `ParseResult` object after using `urllib.parse()` on the URL
*   When **two** command line arguments are given:
    *   The first argument is `StartingURL`, as explained above
    *   The second argument is `MaximumDepth`, a *positive* integer
        *   This parameter controls how far from the `StartingURL` the crawler will travel, it is *not* the maximum number of pages that will be visited
        *   This is the same as the maximum depth of recursion that `crawl()` will reach
    *   When this parameter is *not supplied* or *is not a positive integer*, set `MaximumDepth` to `3`
        *   The program **does not** crash or exit when an invalid `MaximumDepth` is given
*   Extra arguments are ignored
    *   The program does not exit
    *   No message is displayed


### User Interface: Output (10 points)

*   Before calling `crawl()` the first time, print a message stating the starting URL and maximum crawl depth for this run
*   Call `crawl()` and print all links visited from `StartingURL` to `MaximumDepth`
    *   A URL is visited when `requests.get()` is called on it
    *   Your program **must not** print a URL that is not visited
    *   Your program **must not** print the same URL multiple times
*   Visited links are printed with 4 spaces of indentation **per level of recursion**
    *   `StartingURL` is **depth 0**, and is printed *without* indentation
    *   The links found on this page are **depth 1**, and are printed with **4 spaces of indentation**
    *   When the program reaches a distance of 3 links, visited links are displayed with `4 * 3 =` **12 spaces of indentation**
    *   All unvisited links found at `MaximumDepth` are *fetched* with `requests.get()` and their URLs are printed, but **none** of the links found in these pages are visited nor printed!
*   Before the program exits, print a report of the program's activity; the report includes:
    *   the amount of time the program ran
    *   the number of unique links visited
    *   The report is printed even when the program quits on a `KeyboardInterrupt` (e.g. by pressing `Ctrl-C`)
        *   Make the report mention that the user terminated the program early
        *   The count of visited sites may be inaccurate when `Ctrl-C` is pressed; this is not a problem
*   When a problem is encountered in the `requests` and `BeautifulSoup4` libraries, an error message is printed with the current amount of indentation
*   **10 point penalty** if any `print("TODO...")` statements are left in the program
    *   This becomes a **20 point penalty** if a `print("TODO...")` statement is *repeated*


### Handle Exceptions (15 points)

*   Exception Handling protects the crawler from crashing when encountering broken web sites
    *   Exceptions raised by `requests.get()` or `BeautifulSoup` **should not** cause the program to terminate
    *   Instead, an error message is printed and the crawler **proceeds to the next website**
    *   You are **not** penalized if your program hangs on broken websites; there isn't much you can do about this
*   The program gracefully exits upon receipt of `KeyboardInterrupt` by displaying the activity report
    *   It is okay if your program occasionally needs `Ctrl-C` to be pressed a couple times for this to work
        *   The other libraries used by your program will sometimes catch and ignore `KeyboardInterrupt`, depriving your code a chance to respond to it
        *   If you press `Ctrl-C` often enough, you should be able to get your program's attention
    *   Position the `except KeyboardInterrupt:` clause so that the program stops instead of moving on to the next URL
        *   Read the starter code - there is a hint for you in there!
*   Do not *swallow* exceptions; report something about them!


### The `crawl()` function (15 points)

*   `crawl()` must be written as a **recursive** function
    *   This does not mean that `crawl()` cannot use a loop
    *   This means that each step away from `StartingURL` results in a new call to `crawl()`
    *   The return value of `crawl()` may be ignored
*   Use `requests.get()` to fetch HTML content from URIs
*   Use `BeautifulSoup` to find `<a>` tags in HTML content
*   From the `urllib.parse` library, use the functions `urlparse`, `urljoin` and `urldefrag` to manipulate URLs
    *   Fragments are stripped from URLs to avoid duplicate visits
        *   See [What URLs are "the same"?](#what-urls-are-the-same) for more information
*   `crawl()` "remembers" what URLs it has visited with a [set](https://docs.python.org/3/library/stdtypes.html#set)
    *   Python passes mutable data structures by [reference](https://realpython.com/python-pass-by-reference/#passing-arguments-in-python)
    *   This means that changes to the visited set that happen *inside* `crawl()` are visible *outside* of the function without returning it
    *   Any URL your program attempts to fetch with `requests.get()` is considered to be visited, regardless of whether `requests.get()` succeeds or fails
    *   Your program **must not** print a URL that is not visited
    *   Your program **must not** print the same URL multiple times
*   `crawl()` may not use global variables
    *   Modify `crawl()` to take more parameters, such as:
        *   `url`: an absolute URL
        *   `depth`: the current depth of recursion
        *   `maxdepth`: the maximum depth of recursion
        *   `visited`: a `set` of URLs which have already been visited
*   Supply a starting distance of `0` the first time `crawl()` is called
    *   In other words, the initial URL supplied from the command line is **depth 0**
*   You may supply an empty `set()` for the initial value of `visited`, or you can populate the set with some URLs to *never* visit
    *   One reason you might do this is to avoid websites that make your program behave badly.
*   Each time `crawl()` is called:
    *   If the current value of `depth` exceeds `maxdepth`, immediately return
    *   If the given URL has been `visited`, immediately return
    *   If the given URL is invalid, immediately return
        *   `requests.get()` works only with absolute HTTP/HTTPS URLs
    *   If everything is good
        *   Print out the URL passed in through the `url` parameter
            *   Refer to the `depth` parameter to see the current depth of recursion
            *   Use indentation to indicate the current depth of recursion.
            *   Print **four spaces** for each level of recursion (see the [sample output](Output.md))
            *   **Do not** print tabs `\t`; print **four spaces**
        *   Mark the url that is about to be visited as `visited`
            *   An attempt to visit a url counts as a visited url for our purposes; no need to try failed urls again later
        *   Use the **requests** library to fetch the webpage by `url`
        *   Print any exceptions that are raised and return from this invocation of `crawl()`.
            *   Your program *must not crash* when an unavailable resource is encountered.
        *   Scan the resulting HTML for anchor tags `<a>`.
        *   `for` each anchor tag:
            *   Check for an `href` attribute; if this anchor tag doesn't have one, `continue` to the next iteration of the loop.
            *   Discard the *fragment* portion of the URL, if present.
                *   One of the libraries utilized might have something to help with this...
            *   Determine whether the `href` attribute refers to an absolute URL.  If not, make it into an absolute URL by using the `urljoin()` function and the current value of `url`
                *   One of the libraries utilized might have something to help with this...
            *   Call `crawl()` again recursively with appropriate parameters
                *   Don't forget to increment `depth`!


## Software libraries

As Fred Brooks Jr. writes in *No Silver Bullet*, one of the biggest
advancements of modern software engineering is the availability of libraries of
pre-written code.  Reusing well-crafted code enables us to create bigger, more
reliable and more featureful systems faster and more cheaply than writing every
line of code from scratch.  Software engineers spend a considerable fraction of
their time learning how to incorporate new libraries into their projects.

I have included demo programs under the `demo/` directory to help you learn the
libraries needed in this assignment.

#### [urllib.parse](https://docs.python.org/3.9/library/urllib.parse.html) Python's Standard URL Parsing Library

*This library is part of the Python standard distribution and does not need to be installed manually.*

The `urlparse()` function can be used to evaluate whether a URL is absolute and thus suitable for use with `requests.get()`.

```python
from urllib.parse import urlparse
parsed = urlparse('https://cs.stanford.edu/~knuth/news.html?query=The Art of Computer Programming#this-is-a-fragment')
print(parsed)

ParseResult(scheme='https', netloc='cs.stanford.edu', path='/~knuth/news.html', params='', query='query=The Art of Computer Programming', fragment='this-is-a-fragment')
```

See the [urlparse.py demo program](../demo/demo_urlparse.py) for a more complete demonstration.


The `urljoin()` function combines an absolute URL with a relative URL,
resulting in a new absolute URL.  When two absolute URLs are joined, the paths
are matched as far as they are the same.

```python
from urllib.parse import urljoin
absPlusRel = urljoin('https://cs.stanford.edu/', '~knuth/musings.html')
print(absPlusRel)

https://cs.stanford.edu/~knuth/musings.html

absPlusAbs = urljoin('https://cs.stanford.edu/~knuth/vita.html', 'https://cs.stanford.edu/~knuth/graphics.html')
print(absPlusAbs)

https://cs.stanford.edu/~knuth/graphics.html
```

See the [urljoin.py demo program](../demo/demo_urljoin.py) for a more complete demonstration.

This library also includes a function called `urldefrag()` that strips fragments from a URL.  It works like this:

```python
from urllib.parse import urldefrag
url = "https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urldefrag"
defragged = urldefrag(url)
print(f"defragged = {defragged.url}")
```

You can use it if you want, but it is just a fancier way to do this:

```python
url = "https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urldefrag"
defragged = url.split('#')[0]
print(f"defragged = {defragged}")
```



### 3rd Party Libraries

You only need these libraries to complete this assignment.  In fact, your
program should **not** use any other libraries because of the extra work it
creates for the graders.

These libraries can be installed on your system by navigating into the repository in a command shell and running

```bash
$ python -m pip install --user -r requirements.txt
```

Be sure to note in your User's Manual that your program requires these software libraries.


#### [Requests](http://docs.python-requests.org/en/master/) HTTP Library

A simple interface to making HTTP requests from a Python program.

```python
import requests
r = requests.get('http://checkip.dyndns.com')
print(r.text)

<html><head><title>Current IP Check</title></head><body>Current IP Address: 13.103.37.144</body></html>
```

See the [requests.py demo program](../demo/demo_requests.py) for a more complete demonstration.


#### [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) HTML Parsing Library

BeautifulSoup uses a pluggable HTML parser to parse a (possibly invalid)
document into a tree representation.  BeautifulSoup provides methods and
Pythonic idioms that make it easy to navigate, search, and modify the parse
tree.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><head><title>Current IP Check</title></head><body>Current IP Address: 13.103.37.144</body></html>")
text = soup.find('body').text
print(text)

Current IP Address: 13.103.37.144
```

See the [beautifulsoup.py demo program](../demo/demo_beautifulsoup.py) for a more complete demonstration.

## Absolute and Relative URLs

An absolute URL contains enough information by itself to locate a resource on a
network.  It includes, at minimum, a scheme followed by the token `://`
followed by a hostname.

The **scheme** (a.k.a. protocol) is the `http`, `https`, `ftp`, `telnet`, `ssh`,
etc. which may occur before the `://` token (when present).  This indicates how
the client program (i.e. your web browser or the `crawl.py` program) will
communicate with the server.

The **hostname** comes after the optional `scheme://` at the beginning of a URL and
before the next `/` character.  A hostname identifies a machine on the
internet.  The hostname may be a plain IP address or a human-friendly string
that can be resolved to an IP address.

Following the hostname may come the optional components **path**, **query
parameters** and/or **fragment**.

### Examples of Absolute URLs

*   `https://duckduckgo.com`
*   `https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/instructions/README.md`
*   `https://usu.instructure.com/courses/547414/assignments/2698431?module_item_id=3503120`
*   `http://dwm.suckless.org/tutorial/#content`


### Examples of Relative URLs

*   `duckduckgo.com`
    -   A hostname only, no scheme
*   `erik.falor/cs1440-falor-erik-assn6/-/blob/master/instructions/README.md`
    -   No scheme nor hostname
*   `assignments/2698431?module_item_id=3503120`
    -   No scheme nor hostname, only a partial path
    -   The presence of query parameters don't affect whether this URL is absolute or not
*   `#content`
    -   A fragment-only relative URL which refers to back the same page it is found on
    -   A URL like this should be ignored by your program

Many resources presented on websites are referred to by a relative URL, which
leave off one or more of these components.  When a relative URL is encountered,
the client combines the corresponding information from the current document to
convert the relative URL into an absolute one.  Your `crawl()` function must
therefore know the URL of its current document so that it can substitute
missing information into relative URLs.

For example, if you point your program at `http://cs.usu.edu` and encounter a
link to `/articles.aspx`, your program will convert this to the absolute URL
`http://cs.usu.edu/articles.aspx` by means of the `urljoin()` function from the
`urllib.parse` library.


### Fragment Identifiers in URLs

A part of a URL occurring after a `#` symbol is known as a fragment, and refers
to a sub-section within a document.  Your program is concerned only with entire
documents; either a document has been visited or it has not.

Fragments should be removed from an absolute URL before checking whether it has
been visited before or not.

All relative URLs beginning with `#` refer to another location within the
current document.  Because your program should not visit the same document
twice, such URLs should be discarded.


## What URLs are "the same"?

You may find examples with your browser that don't match these rules.  These rules apply to this web crawler.

-   URLs with and without a trailing `/` are *different*
    -   e.g. your program treats `http://unnovative.net` and `http://unnovative.net/` as **different** sites
-   URLs beginning with `http://` and `https://` are *different*
    -   e.g. your program treats `http://cs.usu.edu` and `https://cs.usu.edu/` as **different** sites
-   URLs which differ only in their fragment are *the same*
    -   e.g. your program treats `http://unnovative.net`, `http://unnovative.net#hello` and `http://unnovative.net#goodbye` as **the same** site


## Testing your Crawler

You need to turn this program loose on the internet to find out if it works.  To keep this program really simple, it does not honor the [Robots Exclusion Standard](https://www.robotstxt.org/).  `robots.txt` is a file found on servers which contains rules that an automated web crawler is supposed to follow.  Because your crawler doesn't look out for these files, this means that a visit by your crawler could be regarded as malicious.

So far, no DuckieCorp interns have gotten into trouble while working on this project.  To keep it that way, try to restrict your testing activities to

*   The [Testing Server](../demo/Using_the_Testing_Server.md)
*   https://cs.usu.edu
*   Websites that you personally operate
*   Websites that you have explicit permission to crawl

Of course, as your crawler visits these sites it will inevitably follow links to other sites outside of this set.  This is okay, and you won't get into trouble as long as your crawler's activities don't become noticeable to the site admin.

**TL;DR:** Don't hammer an unsuspecting site with an unreasonable amount of automated traffic.
