# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
This program will take a directory, then read the 2021.annual.singlefile.csv and area-titles.csv files and supply the desired information into the report
it will run in any current working directory, read all the fips and give requested data through the report function
Given a proper Directory containing these files, the program will read them and sort out the large amount of data, and then report it back to the user
### Things I know how to do:
* open files
* read files line by line
* Use data within lines to sort them out
* pass data to report function
* Read fips, only somewhat understand but enough to do assignment 
### Some challenges I may face
*  Understanding all of what I need to know and do, due to the data being so large
* Stress about length of file, and if I need to make new tools
* Placing proper tags, and giving myself time.
## Phase 1: System Analysis *(10%)*
### Inputs
* Arguments (File directory)
### Outputs
* Final Report data from directory
* Error Reports / usage of function
### Some needed Functions
* areaTitleData
  * read area title data and sort between wanted and unwanted data using fips, then save wanted data for later
  * #### Inputs
    * directory to find file in
  * #### Outputs
    * N/A
* annualSinglefileData
  * open 2021 single file find data for all lines in pertaining to wanted data, then send all applicable data to report; such
as industry code, own code, total annual wages, annual employment level and establishments in both soft and industrial
    * #### Inputs
      * directory to access file?
    * #### Outputs
      * N/A
* report       #function already given#
  * order data given then print it out
  * #### Inputs
    * receives data from other functions
  * #### Outputs
    * Prints out a form with specified data
## Phase 2: Design *(30%)*
### read area title data and sort between wanted and unwanted fips codes
* areaTitleData(directory)
  * open area-titles.csv in given directory
  * read area-titles line by line
    * sort out included and excluded areas using fips
    * if line is included:
      * then save to list or dict
    * if not:
      * continue to next iteration in loop
  * close area-titles.csv
#### Good Input
1. Receives directory containing area-titles.csv 
2. Opens area-titles.csv
3. Reads and sorts applicable lines 
4. Closes area-titles.csv 
5. Returns a dictionary of fips and their locations
6. Function finishes
#### Bad Input
1. Receives directory that does not contain  area-titles.csv 
2. Invalid file error from open function is given to user
### read annual file data then give all data applicable to final report
* annualSinglefileData(directory, includedFips)
  * open 2021.singlefile.csv in given directory
  * read 2021.singlefile.csv file line by line
    * if line starts with applicable fips code:
      * split line into parts to separate data
      * if line industry code = "10" and own code = "0":
        * then update all industries data on report
      * if line industry code = "5112" and own code = "5"
        * then update software publishing industry data on report
      * if NOT:
        * go to next line
    * if it doesn't start with included fips code:
      * move on to next line
  * close 2021.singlefile.csv
#### Good Input
1. Receives directory containing file 2021.singlefile.csv and valid list of Fips
2. Opens 2021.singlefile.csv 
3. Begins reading every line, and identifies if line should be used
4. Adds usable data to applicable report attributes
5. Closes File
6. Function finishes
#### Bad Input
1. Case1:Receives Directory that does not contain 2021.singlefile.csv Case2:Fips list is empty
2. Case1:Attempts to open 2021.singlefile.csv and runs into error. Case2: outputs("Error: No Applicable Fips codes") and then exits program
## Phase 3: Implementation *(15%)*

* Added in a lot of variables and checking functions as I forgot to include proper checking and initialization of variables, like includedFips as well as checking for max vs new max
* I also realized that a lot of the data has "" so I had to work that into commands like str.endswith('000"') to filter out 
the excluded fips codes.
* Everything else went pretty well, just fixing up some formatting stuff that I missed on my first passthrough


## Phase 4: Testing & Debugging *(30%)*
I only found a couple of errors in my code while implementing, such as specific cases in the fips codes, however I did not find any major bugs.
#### General Testing:
* All the instruction test cases such as:

``` python src/bigData.py data/UT_complete ```
* First ran the program through DC's and HI's test sets that I made using the instructions
* After verifying it all was the same, I proceeded to test only the _complete data sets, as they have both the all_industries and software_industry data.
#### Empty directory or Directory not containing one of the files:
* create directory and then run to test if working
* result:
``` 3$ python src/bigData.py data/emptyDirectory                        
Reading the databases...                                                                                             
Traceback (most recent call last):                                                                                     
    File "\\wsl$\Ubuntu\home\price373\cs1440-hansen-dalton-assn3\src\bigData.py", line 100, in <module>                    
        includedAreas = readAreaTitles(sys.argv[1])                                                                        
    File "\\wsl$\Ubuntu\home\price373\cs1440-hansen-dalton-assn3\src\bigData.py", line 39, in readAreaTitles               
        areaFile = open(fileDirectory)                                                                                   
FileNotFoundError: [Errno 2] No such file or directory: 'data/emptyDirectory/area-titles.csv'  
 ```
* The partial correct data just lets the other open() crash instead
#### No input directory given:
* run program without any additional arguments
* result:
```
Argument Error: bigData.py takes exactly [1] Argument                                                                                   
Usage: bigData.py FILE_DIRECTORY
```
#### Too many Arguments:
* Give program additional directories.
* result:
```
Argument Error: bigData.py takes exactly [1] Argument                                                                                   
Usage: bigData.py FILE_DIRECTORY
```

## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance

* Honestly I think that my report update statements are a little sloppy, or maybe just hard to read.
  * All in all, none of the code is too hard for me to understand, and with a little bit of time and effort I knew what to do
  * If a bug is reported in a few months, I might put in a todo list, but it might take me a while to both get around to it and find the cause after a long time of not working on it
* I Believe that my documentation is fairly easy to understand, however that could just be a misconception from me
* Adding more functions to this program shouldn't be too hard, as it is somewhat modular in design.
* My program should not have problems with many of the changes, unless a major overhaul of either my OS or of python takes place
