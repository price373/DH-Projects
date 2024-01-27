# Fractal Visualizer User Manual
### How to Run the program
To display a chosen fractal, type the file directory of a chosen fractal (.frac) and a chosen color Palette Name. If no arguments are chosen then it will default to the Mandelbrot Seahorse picture
Here is an example of running the code to create variation using the Phoenix algorithm a peacock fractal with the coldPalette palette of colors:
* ### Figure 1
```commandline 
python src/main.py data/peacock.frac coldPalette
```
### Fractal Algorithms:
* Mandelbrot: starfish, seahorse, mandelbrot etc.
* Phoenix: peacock, monkey-knife-fight, phoenix, etc.
* MandelbrotCubed
* spider
### Palette Choices
* dynamicPalette
* coldPalette
* royalPalette

To create more fractals all you have to do is replace peacock.frac in the example above with a different chosen .frac file.
### What you should see
If used correctly, as seen in figure 1, there should be 2 things happening:
   * A window drawing the chosen fractal with the chosen palette appears.
   * A command prompt output showing the progress of creating the fractal.

If an invalid argument is given an runtime error message will be displayed. If only one argument is given it is treated as the fractal (.frac) file and the default color palette object, royalPalette will be used.
The program will exit when a potential problem may occur, such as an invalid file, so if program does crash, it is somewhat likely to be some sort of error with the argument factors.
