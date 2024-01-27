# Bingo! User Manual  	         	  
This program will create a deck of randomized bingo cards with directions from the user. For example, if you want 24, 6 by 6 bingo cards with the maximum number on the card being 400, then you run the program, and it will prompt you for desired dimensions, amount of bingo cards on the User, and max number on cards. Interface.
## Running The Program
1. `Ensure that the terminal's current directory is in the project directory!`
1. In the terminal run `bingo.py` using the python command. 
   2. if you are not in the primary directory, use a relative directory to src in the project file.
``` 
$ python src/bingo.py   
 ########   ####  ##    ##   ######     #######   ####
 ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
 ##     ##   ##   ####  ##  ##         ##     ##  ####
 ########    ##   ## ## ##  ##   ####  ##     ##   ##
 ##     ##   ##   ##  ####  ##    ##   ##     ##
 ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
 ########   ####  ##    ##   ######     #######   #### 
 
    Welcome to the DuckieCorp Bingo! Deck Generator                          
    Main menu:                                                                                                           
    C) Create a new deck                                                                                                 
    X) Exit the program   
```

## Menu And Functionality
### Menu and Interface
As you can see in the demonstration above the UI prompts for "C" to create a deck or "X" to exit the program, none of the menu prompts are case sensitive. If the user selects the option to create a deck, then a similar menu prompt shows options for the deck before generating it, such as deck size and bingo card dimensions. After the deck is generated the user will be asked what they want to do with the deck, the new prompt will be "P" for print a single card. "D" to display the whole deck. "S" to save the entire deck to a file. And "X" to return to the Main menu.
### Small Details
* A deck will be saved until either the program is ended, or a new deck is generated.
* Every bingo card is saved to its card number until the deck is deleted.
## Common Errors and How to Fix Them
Some Errors that may be seen are an invalid file path when saving the deck, Invalid inputs like "c" rather than the correct option "C", or a number exceeding maximum values of deck size or card size.
Most of these are fixed just by correcting the response, like providing a valid file directory.

