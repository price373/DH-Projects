# Code Smells Report - 5.0

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Copy the offensive code between `` ``` ``
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!


### These are some of the code smells you may find in the starter code:

0.  **Magic** numbers
    *   Numeric literals in critical places without any context or meaning
    *   "Does `256` over here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
2.  **Poorly-named** variables
    *   Short variable names are okay in some contexts:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share **too much information**
    *   When almost every line of code is has an explanatory comment, it is likely true that variable and function names were poorly chosen
    *   Write code that speaks for itself
4.  Comments that **lie**
    *   An out-of-date remark that longer accurately describes the code
    *   Bad advice left by a developer without a clue
5.  Too many arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but left unused
    *   Instead, accumulate parameters into a collection such as a dict
6.  Function/Method that is too long
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"
7.  Complex decision trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Has every branch been tested?
8.  Spaghetti code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of 
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   A repeated statement which doesn't have an effect the second time
    *   ```
        i = 7
        print(i)
        i = 7
        ```
    *   Ask yourself whether it makes any difference to be run more than once.
10. Dead code
    *   A piece of code that is not used (usually because it is obsolete)
    *   Blocks of commented-out code that serve no purpose and clutter up the file

If you see something that is not covered on this list, please add it to this report.


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 32, 34]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first.
    *   ```python
        import mbrot_fractal  	    	       
        import phoenix_fractal as phoenix  	    	       
        import mbrot_fractal  	    	       
        ```
    *   This is easily resolved by deleting the second `import` statement.
    

## Code Smells
0.  Magic number "512" at 'src/mbrot_fractal.py' [lines 226, 232, 235, 236, 238, 243, 245, 252, 253, 343]
   *   The number "512" is used in 10 lines of code, and lack context for the use of said number, excluding when used in lines 343 and 226 where width and length are assigned 512 in the canvas or Photo image.
       ```python
            
        pixelsize = abs(maxx - minx) / 512  	    	       

        portion = 0  	    	       
        total_pixels = 512 * 512  # 262144  	    	       
        for row in range(512, 0, -1):  	    	       
           cc = []  	    	       
        for col in range(512):
        ```
   * This can easily be supplemented by setting a size variable relating to the window size (i.e windowSize = 512)
1. Global Variables at 'src/mbrot_fractal.py' [lines 156, 159, 160]
   *   The Variables z, MAX_ITERATIONS, and iter are used as global variables. Many of these global variables are not really used for much outside of functions where they are reassigned constantly, or are used as constants that could be passed into the function as an argument to cut down on repeated use of a nonlocal variable.
        ```python
         global z  	    	       
        z = complex(0, 0)  # z0  	    	       
 
        global MAX_ITERATIONS  	    	       
        global iter  	    	       

        len = MAX_ITERATIONS 
        ```
   * With the constant we can just pass the value into the function rather than try to keep track of what the variable is and isn't. With the others we can just use local variables because they are reassigned very often inside of the functions.

2. Poorly-named variables at 'src/phoenix_fractal.py' [line 63, 75]
   *   We have a variable called c that describes the Julia Constant and the argument z, but if you see the variables 'c' or 'z' further in the code it is unclear of what is actually represents.
   ```python
         c = complex(0.5667, 0.0)
    ```
   ```
    def getColorFromPallette(z):
   ```
   * We just have to change the name of this variable to become self-documenting, so that it isn't confusing to future developers.

3. Comments that share too much are at 'src/pheonix_fractal.py' [lines 74, 77, 80, 81]
   * These comments like the comment for variable 'c' just share information about the reason why the variable is important/what the variable is as well as overexplaining self-explanatory variables.
    ```python
    # c is the Julia Constant; varying this value gives rise to a variety of variated images  	    	       
    c = complex(0.5667, 0.0)  	    	       

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results  	    	       
    pheonix = complex(-0.5, 0.0)  	    	       

    # The first thing we do to the complex number Z is reflect its components,  	    	       
    # so the imaginary part becomes the real part, and vice versa  	    	       
    zFlipped = complex(z.imag, z.real)  	    	       
    ## if we don't do this, the image comes out SIDEWAYS!!!
    ```
    * Although not the worst, these comments are either useless or are justifying a poorly named variable like c in the above example.

4.  A comment that lies is at 'src/main.py' [line 56,57]
    * This comment says that the program quits if it gets too many arguments then the program will quit, however the if statement only works when there are less than 2 arguments, where running the program is one already.
    ```python
    # quit when too many arguments are given  	    	       
    if len(sys.argv) < 2:  	    	
    ```
    * This comment should either be removed as it is invalid or changed to properly portray what the program does.
5.  Too many arguments are passed at 'src/mbrot_fractal.py' [lines 251 - 261]
    * This function receives 2 arguments(rows and cols), but only uses one of them. So why have the second argument?
    ```python
    def pixelsWrittenSoFar(rows, cols):  	    	       
        portion = (512 - rows) / 512  	    	       
        pixels = (512 - rows) * 512  	    	       
        status_percent = '{:>4.0%}'.format(portion)  	    	       
        status_bar_width = 34  	    	       
        status_bar = '=' * int(status_bar_width * portion)  	    	       
        status_bar = '{:<33}'.format(status_bar)  	    	       
        # print(f"{pixels} pixels have been output so far")  	    	       
        # return pixels  	    	       
        # return '[' + status_percent + ' ' + status_bar + ']'  	    	       
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
    ```
    * This can be fixed by simply removing the cols as it is unused and not needed.
6.  The function makePictureOfFractal at 'src/phoenix_fractal.py' [lines 128 - 211]
    * This function is very long, with many comments and has a lot of functions from creating the window to filling the window with the image and displaying pixel count.
    ```python
        cp = getColorFromPalette(complex(x, y))  	    	       
        cs.append(cp)  	    	       
        pixls = '{' + ' '.join(cs) + '}'  	    	       
        p.put(pixls, (0, s - r))  	    	       
        w.update()  # display a row of pixels  	    	       
        fraction_of_pixels_writtenSoFar = (s - r) / s # update the number of pixels output so far  	    	       
        # print a statusbar on the console  	    	       
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	    	       
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  	    	       
                end="\r"  # the end  	    	       
                , file=sys.stderr)  	    	       
        r -= 1  	  
    ```
    * this could be fixed fairly easily by breaking it down into functions like a paint function and a window function seperately.
7. A complex decision tree is at 'src/mbrot_fractal.py' [lines 166 - 190]
    * This tree of statements has many branches with < or > statements, but several of these can be done in one elif condition. Also what work does a condition do when it doesn't do anything for the program?
   ```python
        if abs(z) > TWO:  	    	       
            z = float(TWO)  	    	       	    	       
            import builtins  	    	       
            len = builtins.len  	    	       
            if iter >= len(palette):  	    	       
                iter = len(palette) - 1  	    	       
            return palette[iter]  	    	       
        elif abs(z) < TWO:  	    	       
            continue  	    	       
        elif abs(z) > seven:  	    	       
            print("You should never see this message in production", file=sys.stderr)  	    	       
            continue  	    	       
            break  	    	       
        elif abs(z) < 0:  	    	       
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
            sys.exit(1)  	    	       
        else:  	    	       
            pass
   ``` 
   * This is resovled by consolidating the two statements that are not supposed to happen, and remove unneccessary branches like the else statement here, that doesn't actually do anything.
8.  There is Spaghetti code at 'src/main.py' [lines 85 - 119]
    * This code and the variables used and contain multiple conditions being kept. That just seem very lost and unclear as to many of the reasons they are there. This makes it almost impossible to completely understand what the end goal is and why it is written this way.
    ```python
    
    ```
    * A lot of this code could be fixed by using simple conditions and rewriting the loops into a single loop using a if statement to differentiate or rewrite into another part of the code.
    * Another option would be to create a list that contains all the names of available fractals.
9.  Redundant code can be found at 'src/phoenix_fractal.py' [lines 157, 158, 159, 171]
    * the function tk_Interface_photoImage_canvas_pixel_object.pack() is used several times here, and doesn't seem to change anything as the .pack method should only be needed to called once
    ```python
    tk_Interface_PhotoImage_canvas_pixel_object.pack()    	    	       
    tk_Interface_PhotoImage_canvas_pixel_object.pack()     	       
    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    ```
    * This can easily be fixed by just removing the excess statements as they don't actually affect the program.
10. There is some dead code in 'src/mbrot_fractal.py' [lines 123 - 152] 
    * This code block is not being used, because it is commented out so what use does it have, especially with a complete rewrite of the function.
    ```python
    # def colorOfThePixel(c, palette):  	    	       
    #     """Return the color of the current pixel within the Mandelbrot set"""  	    	       
    #     global z  	    	       
    #     z = complex(0, 0)  # z0  	    	       
    #  	    	       
    #     global MAX_ITERATIONS  	    	       
    #     global iter  	    	       
    #  	    	       
    #     len = MAX_ITERATIONS  	    	       
    #     for iter in range(len):  	    	       
    #         z = z * z + c  # Get z1, z2, ...  	    	       
    #         global TWO  	    	       
    #         if abs(z) > TWO:  	    	       
    #             z = float(TWO)  	    	       
    #             if iter >= len(palette):  	    	       
    #                 iter = len(palette) - 1  	    	       
    #             return palette[iter]  	    	       
    #         elif abs(z) < TWO:  	    	       
    #             continue  	    	       
    #         elif abs(z) > seven:  	    	       
    #             print("You should never see this message in production", file=sys.stderr)  	    	       
    #             continue  	    	       
    #             break  	    	       
    #         elif abs(z) < 0:  	    	       
    #             print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
    #             sys.exit(1)  	    	       
    #         else:  	    	       
    #             pass  	    	       
    #  	    	       
    #     return palette[iter]  # The sequence is unbounded  	    	       

    ```
    * These pieces of code can be resolved very easily as they are just not needed or used, so we just have to delete them.