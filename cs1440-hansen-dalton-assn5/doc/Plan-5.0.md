# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**
* I am tasked with refactoring the programs given in the src directory into refined and modular code while not changing the output. While it seems simple I first need to identify code smells and how I could fix them, then I need to fix them along with making new tests and fixing the old ones to match the new code.
    * For example splitting up the driver and 2 modules to a driver and 5 modules to more easily keep track of data and variables in use
    * Also I need to improve the documentation of this project to make future edits and additions
* The program itself is drawing fractals using math, and TKinter, and I am making it cleaner and easier to modify and add.
    * A good solution should be clean, modular functions and classes, that creates the fractals with colors to show the interesting patterns created by imaginary numbers.
    * I already know a lot of good coding techniques, as well as how to format for easier reading
      * I know how to document and create comprehensive explanations of the code and how it functions
      * I know how to create classes and functions to simplify code and modularize the program
    * I do not really know too much about TKinter and Fractals, so understanding them might be somewhat difficult to work around
    * I also don't really know the full line of thought that the original developer had when making this project, so I need to understand that in depth to better work on the program.
## Phase 1: System Analysis *(10%)*
* Data used in the program
  * Commandline Arguments (sys.argv) 
  * TKinter and its functionalities
  * Modules(mbrot_fractal and pheonix_fract)
  * Some libraries like time and sys
* The output is a % of fractal drawn, and the TKinter window object that draws the fractal on it.
* The use of complex numbers, and the imaginary parts of them plays a big role in this program.
* Using classes and modules to seperate the data and functional pieces such as a program to hold fractal data vs pallette data.
## Phase 2: Design *(30%)*

#### main: driver of the program. Takes arguments and verifies them.
```
import libraries
fractalList = fractalInformation()
def processArgs(args):
    if args is 2 or greater and args[1] is in fractalList:
        chosenFractal = args[1] # Or the one with the fractal name
        return chosenFractal to caller
    else if args is less than 2 or args[1] not in fractal list:
        print("Please provide the name of a fractal as an argument")
        for fractals in fractalList:
            print(fractalName)
        exit with error code
    return None to caller
getFractalData(chosenFractal)
paintImage(fractalInfo)
```
* good: will give chosen fractal and continue the program .
* bad: will quit and give error message with prefered use. Another case is too many arguments, 
where if it is a valid argument in the args[1] slot, then the rest of the arguments will be ignored.
* examples: if "python src/main.py mandelbrot phoenix" is put into command line, the mandelbrot will be drawn but the phoenix won't.
#### ImagePainter: directs other modules to create image
```
import pallette phoenix and mandelbrot 
window = Tk object
WINDOWSIZE = 512 
fractalPicture = PhotoImage(WINDOWSIZE, WINDOWSIZE) 
canvas = Canvas object
pack canvas together with the picture and window objects (pack method)
def paintImage(fractalInfo):
    min coordinates # provided in phoenix module
    max coordinates # " "
    pixelSize = the absolute value of (maxX - minX) / WINDOWSIZE # or the same with max and min Y instead.
    create image with Photo Image object # lets us draw in pixels
    loop for rows: (can use the one  in phoenix_fractal with some minor changes
        loop for columns:
            if fractalInfo('type') is 'mandelbrot':
                color pixels with mandelbrot palette
            elif fractalinfo('type') is 'phoenix':
                color pixels with phoenix palette
        update window and fractalPicture
        imageprogress(number of Rows)
    save fractalPicture as a png
def __imageProgress__(rowNum):
    is essentially already written from pixelsWrittenSoFar from mbrot_fractal.py
```
* good: Will send all required information to functions and methods and prints out progress and displays fractal picture
* bad: Will be unable to identify and retrieve information and will crash "string is not dict" kind of error.
* example: if paintImage receives the mandelbrot dictionary, then it will retrieve and use its information to draw the full picture with no problems
* if __imageProgress__ receives invalid number, then the progress bar will be wrong.
#### Palette: holds palette information and gives said information through functions
```
# These are just arrays of a bunch of colors, but are different for mandelbrot and phoenix fractals.
phoenixColors = ["f00000", "ff9900"...]
mandelbrotColors = ["ff00ff", "ff9900"...]
def getPhoenixColor(count):
    if count >= length(phoenixColors):
        return phoenixColors[length(phoenixColors)-1]
    if count is less than length(Phoenix Colors):
        return phoenixColors[count]
def getMandelbrotColor(count):
    if count >= length(mandelbrotColors):
        return mandelbrotColors[length(mandelbrotColors)-1]
    if count is less than length(mandelbrotColors):
        return mandelbrotColors[count]
```
* good: will return a color value according to count given.
* bad: will run into an index out of bounds error
#### Phoenix: runs iterations of complex coordinate to find total iteration count
```
def getPhoenixIterCount(compCoords #can be called z#, maxIterations # default 101):
    phoenix and c constants
    coordsFlipped = flip complex coordinates
    prevComplex = complex(0,0)
    do this up to maxIterations times:
        iteration count + 1
        saveComplex = coordsFlipped
        coordsFlipped = coordsFlipped * coordFlipped + c + (phoenixConstant * prevComplex)
        prevComplex = saveComplex
        # follow getColorFromPalette on phoenix_fractal for the rest
```
* good: will return iteration count after going through as many as possible
* bad: will run into an error with invalid complex coordinates and cause program to crash.
#### Mandelbrot: runs iterations of complex coordinate to find total iteration count
```
def getMandelbrotIterCount(compCoords #c#, maxIterations # default is 115):
    z = complex 0
    do this maxIterations times:
        track iteration
        z = z * z + compCoords
        if absolute value of z is greater than 2:
            return iteration count
```
good: will return iteration count after going until absolute value of z is greater than 2 or max iterations is reached
bad: will return an error, for invalid complex num, or datatype. Potentially could be a complex of (int, 0).
#### FractalInformation: Keeps track of information of programmed Fractals
```
fractalsDict {'fractal0':{ 'centerX': float, 'centerY': float, 'axisLength': float, 'fractalType': str 'phoenix' or 'mandelbrot'},'fractal1':{ 'centerX': float, 'centerY': float, 'axisLength': float, 'fractalType': str 'phoenix' or 'mandelbrot'}...}
def getFractalData(fractal):
    if fractal is a key in fractalsDict:
        return fractalsDict(fractal)
    else:
        return None

```
* good: will receive and verify key, then return data relating to key.
* bad: will receive an invalid key, then return None.
## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
Most things went well and progressed with little to no problems, however there were a couple of times that I forgot to remember return
statements or print statements in my design, however a lot of the things that I missed were in the original code so it was fairly easy to realize.

There was one big problem that I found where I used the wrong variable in my calculation that screwed up my entire display
so that was stressful, but all in all I learned a lot about tkinter, refactoring, and fractals.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   Example:
    ```
    # Command: [Command you ran in the shell]
    # Bug Found: [If the test failed, what was the output?  Keep it brief]
    # Bug Fixed: [Your solution]
    ```
phase 2: Wrote Tests to validate variables and functions are working properly when given a specific function, so receiving data
when asking for 'mandelbrot' set but receiving None when asking for 'mandbrot'
#### Unit Tests
* test_FractalData(): test that the data is retrieved succesfully
* test_dictionaryGetter(): test the getFractalData function
* test_colorOfThePixel(): test the chosen color with a baseline
* test__imageProgress__(): verify image progress function works properly
* test_palleteLength(): verify length of Palette lists
* test_processArgs(): confirm proper function
* test_FractalDicts(): Ensures that select dictionaries are correct and amount of Fractals in FractalInformation
```
# Command: cmp leaf.png before-leaf.png
# Bug found: None
# Bug Fixed: None
# Conclusion: No difference was found between the before and after refactoring pictures.

#
```
Other than the error that I ran into in Implementation, I didn't really run into many errors
## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

I feel like most of my code is pretty well written, but maybe that is a personal bias. However the fractal variable might be a little hard to understand
* There are definitely parts of my code that I don't fully understand how they work, for example the canvas and pixelSize parts.
* I would like to believe that if a bug is reported that I will be able to do it in a few days, but that is probably unrealistic for me, as it might take months.
* I think my documentation is alright and most developers should understand, however I also could've included more comments for clarification.
* Now that the program is modularized, it should be easy to add new features, as well as tests for those features.
* Yes it will continue to work, as long as nothing too major changes between versions, that invalidates the functions themselves. Tkinter not being supported in python for example.