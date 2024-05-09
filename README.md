Pokedex.py is a python program used to store, edit, and print Pokemon objects.
Can be used to either record a brand new pokedex (if you wanted to create a fan game), or to keep track of your pokedex completion in a main series game.
	It performs the latter function by returning whatever entry is the next missing entry, so one doesn't have to run through menus to find it.

The Pokemon object started out as a piece of another project I have planned for the future, involving an AI playing through an old Pokemon game. 
	It stores info such as the species, both types, and the Dex number of the pokemon.
	This object also has values stored for stats and will probably have more when that future project starts progressing.

This program has been updated to store Pokemon data in an Oracle SQL database instead of a text file.
All of this is able to be run directly from your command line as long as python is installed on your PC. 
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

update_dex:
connects to db
updates existing records in Pokedex table

insert_dex:
connects to db
inserts new records to Pokedex table

upload_dex: 
connects to db
creates Pokedex table if needed, and calls insert and update functions
this is executed at the end of the program

download_dex:
connects to db
pulls records from Pokedex table and creates Pokedex dictionary
this is executed when program starts
##############################################################################################################################################################

This was primarily created for fun and for practice with the python language. This project will be expanded upon in the near future when I practice integrating SQL into python through software like pandas. 

