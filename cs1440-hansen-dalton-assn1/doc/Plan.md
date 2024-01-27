# Software Development Plan

# Phase 0: Requirements Specification *(10%)*

## **Deliver:**

*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

## Documentation For This Phase
Use the given duckieEncrypter.py to identify how to create a decrypter. So identify the encryption style used and 
use the given starter code as a beginning.
I kind of know generally how to use, and do the encryptions however I need to look at the code and come up with a 
solution through effective planning. There will be some challenges like bugs and unknown python commands, however 
not anything that should be a major setback.
A good solution should be able to take any duckiecrypted file and decrypt it.
# Phase 1: System Analysis *(10%)*

## **Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

## Documentation For This Phase
User Inputs: File to decrypt. 
The output will be formatted the same as the decrypted file, but in text from instead of duckiecrypt
We will use asciii characters and their numerical values to keep the letters uniform as well as identifying what is letters what are 
other asciii characters and what is not in duckiecrypt. 
Functions to use: .read() .split() and other file and text editing code

# Phase 2: Design *(30%)*

## **Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

## Documentation For This Phase
#Function to Receive and process user file
def processFile(filePath):
    verify legitimacy of given file
    if file is ok to access
	open file
        return open file
    if not
	display error message
	exit safely 
Examples:
good:
	path = "c:\user\Dad\Desktop\secretFile.txt" #we will be using a relative directory#
	file = processFile(path)
sets file variable equal to the open file
bad:
	path = "email.txt"
	display error message
	exit program
#Send character to be decoded
def decryptCharacter(character):
     identify character type (asciii stuff)
     if lowercase:
	remove lowercase symbol
	convert to lowercase character
     elif uppercase
	remove uppercase symbol
	convert to uppercase character
     elif special
	remove special symbol
	convert to special character
     else:
	character = ""
     return character
good:
	currentChar = "^5"
	currentChar = decryptCharacter(currentChar)
	print(currentChar)
	'F'
bad:
	currentChar = "dd"
	currentChar = decryptCharacter(currentChar)
	print(currentChar)
	''
#decrypt a single line# 
def decryptLine(Line): str
    create list out of line
    for characters in linelist:
	decrypt character
should decrypt every single character by using other functions
#convert duckiecrypt character to lowercase
def convertToLowerChar(character):str
	use number to identify letter
	return decrypted character
receive encrypted character and changes it to ascii letter, bad input shouldn't be place into this piece.
#convert duckiecrypt character to uppercase
def convertToUpperChar(character):str
	change number to ascii num
	return decrypted char
receive encrypted character with uppercase symbol and changes it to asciii, bad input should not be able to reach this code
#convert duckiecrypt character to special char
def convertToSpecialChar:str
	identify which group character is in
		if group A:
			remove A
			read char
			calculate which char
		#repeat for B and C/ or any other groups
		if B:
			
		if C:
			
Receives character with special symbol, removes special symbol, Identifies which group character is in, then converts character to special char
#Main Line#
def Main(filePath): str
	get file and verify its input
	send every line through decryption
		printLine
	close file
# Phase 3: Implementation *(15%)*

## **Deliver:**

*   (More or less) working Python code in `src/`.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
    *   If you have nothing of note in this section, **note that you had nothing to note here, do not leave it blank.**

## Documentation For This Phase
I changed my placement of some small syntax and calculations to places that made more sense to me. Also I relearned some things that 
I learned in the lessons, but quickly forgot.

# Phase 4: Testing & Debugging *(30%)*

## **Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

## Documentation For This Phase
When I began testing, I realized I changed the way that os was imported so I had to modify the current directory code to accomadate for that change
I also had a few errors, mainly just forgotten syntax or mispelled call.
I have run some test cases using the given documents in data. I have not run into any errors with normal characters.
I ran into big misidentification errors and bugs with the special tests, and realized that my statements were very open, and could give the wrong outputs. It took me a while to fix all the errors but through nested if statements and else statements was able to rope all of the invalids in.

# Phase 5: Deployment *(5%)*

## **Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.

## Documentation For This Phase


# Phase 6: Maintenance

## **Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?

## Documentation For This Phase
Honestly I feel that a lot of my code is pretty sloppily written, when it comes to the actual decoding, and identifying. I do know 
how all of my code works, but it took me a long time of trial and error to realize it. If a bug is reported in the next few months I feel like I could find the cause quite easily based on how the code is split up.
I think my documentation should make sense, however maybe thats just me. Though I think I was really bad with documenting what functions did what, and where. 
Honestly I don't think that adding anything would be that hard, as my code should stick within its own bounds without causing problems.
Yes, it should have no problems between hardware, software, operating system and python, as far as I am aware.
This assignment was fun but hard. I think I did well enough, however I did not give myself enough time to finish it.
