# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

We are aiming to create a program with classes to create a full deck of functional bingo cards, and give the output to the user along with user interaction
Some things are required such as input validation, as well as variable card sizes, nonrepeating nums on a card, unique column Names, a free space on odd cards, and a way to both print and save decks of bingo cards.
So user can decide to see one card or the entire deck.
So we want a modular class based system driven by user interaction that will both create, save, and print randomized bingo cards with documentation for both users and developers.
#### Things I Know How to Do.
    * I already know generally how classes function and how to implement them into a system like this, and I also know some ways to increment data
    * I also know how to take user input and create an interactive program that can function with directions and output the desired response
    * The random num set and deck classes are at least partially completed and only need small modifications and use of python libraries
#### Some Potential Challenges
    * Adapting to the C++ style code and responding accordingly
    * Creating a function to create a number of objects from the classes based on user input
    * Creating the proper formatted Bingo Cards according to the sizes and data given.
    * Creating a UML Diagram to fully display the design.
## Phase 1: System Analysis *(10%)*

#### Data Used
* M = Maximum number of  that can appear; From user, but range is set
* N = Size of the card 3 to 16; From user, but set range
* RandNumberSet ints
* UI Navigation and decisions; From user
* Number of Bingo cards; From user with set range
#### Output
The output will be a variety of displays in the form of a User Interface(UI) and will give options, print out formatted bingo cards
Or saving a deck to a file on the users directory.

#### Algorithms and Formulae
* Receive and recognize user inputs
* Class initialization and object creation
* Checking and using data in Dictionaries, lists and other data sets.
* Text Formatting
* Recognizing used or unused data, and when to use different
* Class Methods for repeated use
There are some things like class specific formulas like taking data from the random number set or saving classes for future use, however those can get very specific in their algorithms
## Phase 2: Design *(30%)*
### Menu() class:
* Contains MenuOption objects to create a list of options and prompts user for input based on options present.
### MenuOption() class:
* Part of a Menu, receives a character and a descriptive string to display on Menu object
### Deck() Class:
#### Creates and contains Card class objects for further use based on received parameters
    class Deck():
        def __init__:  attributes(__m_card_size,__m_num_cards,__m_max_num, __m_cards)
            for card in __m_num_cards:
                currentCard = Card(card, __m_card_size)
                add currentCard to __m_cards
        def __len__(): int 
            find the length of __m_cards list
        def __getitem(n):
            find card in __m_cards in pos n (where n = card id)
        def __str__(): 
            return __m_cards as a string (.join?)
* good input: will receive all required data and contain a list of Card objects for further use
* bad input: Will not allow bad input past UI, if there is it just won't work
### Card() Class:
#### Stores private data to identify and differentiate between other Card Objects
    class Card():
        def __init__: attributes(idnum, ns):
            initialize data given to local vars
            create array of rows to be modified
        def id(): 
            return idnum
        def number_at(row,col):
            identify value on card at (row, col)
            return value
        def __str__():
            print(self) (Prints singular bingo card)
* Good input: Receives values within bounds of RandNumberSet and initializes Card using those values
* Bad Input: If invalid data is received then it will fail to make card correctly.
### RandNumberSet() Class:
#### Receives numbers to decide sizes and max allowed numbers then returns rows to create Card objects with given row and column sizes.
### UserInterface() Class:
#### Acts as the main program dictating from the user what inputs go where, as well as using the Menu object to create and display options and receive input to give to Deck,Card and other objects. Contains Deck and Menu Objects and calls to print object strings, and save deck to a file.

## Phase 3: Implementation *(15%)*

Everything went well for the most part, however I had quite a few times where I forgot to consider another variable and function so I had to go and do that
The worst one was that I struggled with was making the card with formatting and proper generation.

## Phase 4: Testing & Debugging *(30%)*

I used the given test cases in the testing file, specifically using runTests.py and realized that I had duplicates in my numbers
but I can't figure out how to fix it, so I'll move onto another day.

## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance

Most of my code is pretty sloppily written and there are wide swaths in both Deck and Card that just feel like a jumbled mess of loops and variables.
* I don't quite understand how the RandNumberSet.py works but I was able to use it for the most part
* I probably will forgot about a bug if its reported a few months later.

My documentation is awful, I don't think anyone else, even me in the future will understand what the code does exactly
Adding a new feature should be fairly easy, but that is because of the object oriented nature of this program
Who knows if this program will work after updates and upgrades to hardware and software, but I think it should hold up for a while