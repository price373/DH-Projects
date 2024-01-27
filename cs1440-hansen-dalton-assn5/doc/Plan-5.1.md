# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
We are taking our refactored code and recreating it to become more object oriented using the ideas of encapsulation, polymorphism and abstraction.
The Classes will be broken into superclasses and subclasses. The superclasses being pallette and Fractal. We will need to create 2 new 
fractal subclasses with new ways to handle it. 
This solution leads us to make it easier to upgrade, update and maintain the program along with allowing far easier implementation of new code.
I already know how to do a lot of the object oriented programming and their methods and use, but I think I might struggle with understanding some of the implementation and use of the factory method.
## Phase 1: System Analysis *(10%)*

Quite a lot of the data used within the program (like fractalData, colors, iteration count, file names, etc) is communication between the ImagePainter, FractalFactory, PaletteFactory and FractalParser classes.
* Quick note with the FractalParser class receiving command line input and reading and verifying given files to create
* The regular nominal output will be a display of a fractal, much like the prior state of the program, however it can be decided in the command line to create one using a given format for the fractal.
* So several looping algorithms, such as the ones already present in the program will be rewritten, and the formula used to calculate iterations will be used in the Superclass or Interface for consistent use between all concrete subclasses.
* Additionally Palette names and Fractal files will be received in the commandLine so we must receive and verify system arguments for proper use.
## Phase 2: Design *(30%)*
#### FractalParser: identify correct formatting of .frac files
```
def parseFractalInfo(fracFile):
    file = open(fracFile)
    fracDict
    for lines in file 
        skip lines starting with # and blank lines
        strip all white space
        split on :
        convert key to lowercase 
        assign key to value
        ignore unrecognized items
        if type is phoenix look for creal, cimag, preal, and pimag values
    verifyFractalInfo(fracDict) verify all keys are present
def verifyFractalInfo(fractalDictionary):
    loop to check all required keys are present
```
#### ImagePainter: same as previous, but using changes to how information is received
```
class ImagePainter():
    def __init__(fractal, palette, fractalInfo):
    get min and max values from fractalInfo
    get windowSize from fractalInfo pixels
    initialize window and things for tkinter
    
    def PaintImage(self):
        loop through all x and y values
        use palettegetcolor with fractal.count to get colors for each pixel
        
```
#### Fractal: Abstract class for fractals
```
class Fractal:
    def __init__(maxIterations):
        update maxIterations
    def count(compCoords):
        raise Implement error
```
From here we just replace and add specific numbers for each sublclass replacing count in them.
#### FractalFactory: create a Fractal class using data from file
```
defaultFractal = peacockve dictionary 256 iteration
def makeFractal(fractalInfo):
    take type information and return Fractal class based on it.
```
#### Palette: abstract for palettes
```
class Palette:
    colorList =[]

    def __init__(iterations):
        use iterations number of values in list
    def getColor(num):
        raise implement error
    def getListLength(this.colorList):
        return length of this color list object.
```
similar to the fractals we will fill in these with case specfic implementations and colors with algorithms using % to swap between colors
#### PaletteFactory: create Palette object and return it:
```
defaultPalette = royalPalette object 256 iteration
def makePalette(fractalInfo, paletteName):
    take name and Fractal Info to initalize chosen color palette with a certain size.
    
```
## Phase 3: Implementation *(15%)*
Ended up having to change quite a few variableNames due to the changes I made in the FractalParser so all things relating to\
centerY and centerX were changed to lowercase. Additionally I changed the colorPalettes a little bit from what I planned.
All in all it went pretty well up until the very end, when I realized I had a lot of misnamed variables, and that I forgot to typecast objects properly


## Phase 4: Testing & Debugging *(30%)*
Created 8 tests to test parts of the modules built
* test_colorOfThePixel
* test_palleteLength 
* testImageParameters 
* test_FractalData 
* test_FractalDicts 
* test_processArgs 
* testDefault 
* testFractalCreation



## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance

In all honesty a lot of my code is sloppily written, and could be done significantly better, however I feel like a lot  of the code is fairly self-explanatory
due to Python's nature of coding. If a bug is reported in the future it shouldn't actually take me that long to find the cause of the bug, as my code while sloppy is still segmented into very well defined areas
* I'm gonna be honest my documentation is garbage, like I don't even know if I understand what little amount there is right now.
* It will be easy to add more, but keeping it running after upgrades might be a little bit more of a challenge.