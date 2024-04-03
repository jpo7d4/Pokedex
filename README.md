Pokedex.py is a python program used to store, edit, and print Pokemon objects
Can be used to either record a brand new pokedex (if you wanted to create a fan game), or to keep track of your pokedex completion in a main series game
	It performs the latter function by returning whatever entry is the next missing entry, so one doesn't have to run through menus to find it.

The Pokemon object started out as a piece of another project I have planned for the future, involving an AI playing through an old Pokemon game. 
	It stores info such as the species, both types, and the Dex number of the pokemon.
	This object also has values stored for stats and will probably have more when that future project starts progressing

Overall this is a project to test my skills in data manipulation as well as storing and retrieving data from a file.
Eventually, this same project will be used to do the same with my SQL abilities. 
All of this is able to be run directly from your command line as long as python is installed on your PC 
C:\dir> python Pokedex.py

###############################################################################################################################################################

FUNCTIONS:

new_entry:
Gets information of the new pokemon entry from user input
returns new pokemon object

print_dex:
Prints single requested pokedex entry to screen

menu:
prints main menu options to screen

sort_dex:
sorts the pokedex dictionary by assigning all keys to a list, sorting that list, and then reassigning the pokedex to a new dictionary using that list as key values
ex: newpokedex[listNum] = oldpokedex[listNum]
returns the new pokedex dictionary

find_pok:
finds and prints a pokemon object to screen using the print_dex function
pokemon is determined by user input, accepts either species name or dex number

edit_entry:
finds pokedex entry similarly to find_pok, but then provides options to edit the entry through user input.

find_missing:
finds the next missing entry in pokedex and returns the dex number that would be found at

print_dexfile:
prints pokedex dictionary to a file called Pokedex.txt
formats entries similarly to how they are printed to screen
this is executed at the end of the program

retrieve_dex:
pulls pokedex entries from Pokedex.txt and parses through the text to find values
assigns found values to Pokemon objects and rebuilds Pokedex dictionary
this is executed when program starts
##############################################################################################################################################################

This was primarily created for fun and for practice with the python language. This project will be expanded upon in the near future when I practice integrating SQL into python through software like pandas. 

