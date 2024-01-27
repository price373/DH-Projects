# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

Recreate the shell tools to use in python(don't have to be perfect replicas) and apply it to a variety of files in a way that the user chooses to.
All of the functions work and when they don't work display an error message.
* I know how to make functions
* I know how some of the tools already work like cat paste etc., but not exactly how to implement them
* I know how to read files and both input and output the data of the files.

I will probably struggle at the begginning just kind of seeing where I am, and how I want to do this program, but I think it should be fine from there.


## Phase 1: System Analysis *(10%)*

input takes filePath, file lines, arguments and user input on functions
output will be change of files and printed text with
(Not function but functionality)file reading: gonna have to be able to open the files and read and alter said file
*cat and tac: input:file paths output: print all files, in normal or reverse order, concatenate/display files normally and in reverse
*cut: input: file, arguments output: print changed file or redirect input to other file. remove specific sections of file given.
More small functions, one being an error function.

## Phase 2: Design *(30%)*
#### Driver function
tt.py receives input and redirects arguments to specified tool.
#### Display lines in order for each file#
```
def cat(filePaths):
    for filePath in filePaths:
        file = open(filePath)
	for line in file:
            display(line)
        close(file)
```
good: passes in proper text file prints text of all file lines
bad: passes in inproper text file, 
let open give error
#### Display lines in reverse order for each file#
```
def tac(filePaths):
    for filePath in filePaths:
	    file = open(filePath)
	    fileLines = all lines of file
	    reverse = reverse(fileLines)
	    for line in reverse:
	        display(line)
	    close(file)
```
good: passes in proper text file prints text of all file lines
bad: passes in inproper text file, 
let open give error
#### Search file and return lines of file that match pattern given or line that does not match pattern if specified
```
def grep(pattern, match, filePaths):
    for filePath in filePaths:
	    file = open(filePath)
	    for lines in file:
	        if line have(pattern) and match = "":
		    print(line)
	        elif line nothave(pattern) and match =-k:
		    print(line)
    	    else:
		        next iteration
	    close(file)
```
good: passes in proper arguments and prints all lines that match given pattern, or don't match if -k is given
bad: does not pass in enough args then run usage.py or let open get an error if filepaths are incorrect
#### Read File and return N amount of lines from begginning of the file(10 is default N)
```
def head(-n,N=None, filePaths):
    if user input -n and if N is not described:
        N = 10
    else: #user input -n and N is described
        N = N
    
    for filePath in filePaths:
        if more than 1 filePath in filePaths:
            print("==>" filePath)
        file = open(filePath)
        lines = file.getlines
        #repeat for N amount of times
	    loop N times to print all lines
	        print(lines(currentNum))
	close(file)
```
good: recieves appropriate arguments and file paths get N amount of lines from top of every file and prints them with a heading
bad: does not receive appropriate number of args, then run usage of this tool. if file paths are incorrect open will give error

#### Read File and return N number of lines from the end of the file (10 is default N value)
```
def tail(-n, N, filePaths):
     if user input -n and if N == None:
        N = 10
    for filePath in filePaths:
	file = open(filePath)
	lines = file.getlines
	reverse(lines)
	#repeat for N amount of times
	loop N times to print all lines
	    print(lines(currentNum))
	close(file) 
```
good: recieves appropriate arguments and file paths get N amount of lines from bottom of every file and prints them with a heading
bad: does not receive appropriate number of args, then run usage of this tool. if file paths are incorrect open will give error
(same as head just opposite way)
#### Sort all the lines within the file given
```
def sort(filePaths):
    for filePath in filePaths:
        file = open(filePath)
        for lines in file:
            list add(line)
        close(file)
    sort list items
    for items in list:
        print(item)
```
good: correct file input, receives file, reads the lines passes back a sorted order of lines
bad: incorrect file input then opens error message, in
#### Get wordcount, bytes and line count from file
```
def wc(filePaths):
    for filePath in filePaths:
        file = open(filePath)
        lineList = list of lines in file
        lineCount = length of lineList
        for lines in lineList:
            wordList = line split up at spaces (str.split)
            wordCount += length of wordList
            for words in wordList:
                word --> list
                bytes += num of characters or the length of word
        file(close)
        totalLineCount += lineCount
        totalWordCount += wordCount
        totalBytes += bytes
        print(lineCount, wordCount, bytes, filePath) in seperate columns
    if length of filePaths list is greater than 1:
        print(totalLineCount, finalWordCount, totalBytes, "total") in same columns as other values
```
good:reads files and lines and gives proper output of line count
bad: invalid arguments cause open to give error, or invalid file type will display unexpected data
#### Read File and return desired columns
```
def cut(filePaths, -f, column): #column examples include 1,2  3,6 they are seperated by commas
    seperate column numbers
    sort column numbers
    for filePath in filePaths:
        file = open(filePath)
        for line in file:
            displayValues = []
            for number in column:
                valueList = line split at commas (str.split)
                displayValues.add(valueList[number-1])
            joinStrings(displayValues)
```
good: when given correct args, will grab columns specified after separating them and listing them in the csv format
bad: will display error, or undesirable text based on user input
#### Read file lines placing them into a list then print one line from each file printing with comma instead of newline
```
def paste(filePaths):
    fileList = []
    mostLines = 0
    for filepath in filePaths:
        file = open(filepath)
        add file to fileList
        if file(numLines) > mostLines:
            mostLines = file(numLines)
    for num in range(mostLines):
        displayValues = []
        for file in fileList:
            line = ""
            line = readline(file,num)
            add line to displayValues
        joinStrings(displayValues)
      
``` 
good: given appropriate filepaths, will print lines combined from each file separated by commas
bad: open will have error or does not repeat an appropriate amount of times
###### Sub command for cut and paste to read list given and return a line separated by commas
```
def joinStrings(displayValues)
    newLines = []
    for lines in displayValues:
        newLine variable = lines without new line statement
        add newLine string to newLines list
    print(",".join(newLines))
```
good: receives complete list and prints a string separated by commas in a new line
bad: receives invalid or incomplete data, sends python error or sends back unexpected text
## Phase 3: Implementation *(15%)*

It went well for the most part, however I neglected a lot of planning for taking the arguments that I had to add in.
But for the most part it was pretty easygoing implementation, other than the few formatting hiccups.


## Phase 4: Testing & Debugging *(30%)*
I used the all of the premade functions to give me comprehensible errors so testCat.py, testCut.py testTac.py, testPaste.py,testHead.py
testTail.py, testGrep.py, testSort.py test.WC.py, testUsage.py and testInvalidUsage.py
I found several errors this way including many and I mean MANY list out of index errors and some logic errors on Tail.py
that were giving me invalid responses, so instead of a,b,c it was a,c,b and it took me a while to fix.
## Phase 5: Deployment *(5%)*

*   *Important:* complete **Phase 6** first!
    *   (I know it's backwards, just go with it)
*   **YOU DON'T NEED TO WRITE ANYTHING IN THIS PHASE**
    *   Just follow this checklist
*   **Push** your final commit to GitLab
*   **Verify** that your final commit was received by *browsing* to its project page on GitLab
    *   Ensure the project's *URL is correct*
    *   Review that all required files are present *in the correct location*
    *   Check that unwanted files *have not* been committed
    *   Add *final touches* to your documentation, including the Sprint Signature and this Plan
*   **Validate** that your submission is complete and correct by *cloning* it to a new location on your computer and re-running it
	*	Run your program from the *command line* so you can see how it will behave when your grader runs it
        *   **Testing in PyCharm is not good enough!**
    *   Re-run your *test cases* to avoid nasty surprises



## Phase 6: Maintenance
I think that my Tail, Head, and WC functions are pretty sloppy and uncared for, but I do know how all of them work 
after a lot of time figuring it out
* My documentation might not make sense to other people, or myself in 6 months as I definitely neglected proper documentation
outside the planning doc.
* It shouldn't be terribly difficult to add any new functions as it is already very modular and specialized.
* Honestly I don't know if my program will be able to keep up with updates to things, but as long as nothing changes too 
drastically it really shouldn't be a problem