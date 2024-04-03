'''
Pokedex Project

Program will take in user input to create a dictionary of pokemon (pokedex).
	Include method to update Pokemon data
Functionality will also include pulling that pokedex data from a file so data can be preserved
	Eventually, this will be replaced with an SQL table
Pokedex will be able to be fully printed to screen or to a file
Will include method to find next unknown pokemon in pokedex.


'''


import Pokemon
global Types
Types = ['Grass','Fire','Water','Electric','Rock','Ground','Fighting','Psychic','Ghost','Poison','Bug','Ice','Dragon','Normal','Flying','Dark','Steel','Fairy']

'''
Function Definitions:
new_entry: pulls user input to create new pokemon object. object then gets returned
update_entry: Lets user update a pre-existing pokedex entry
retrieve_dex: pulls dex data from Pokedex.txt
find_pok: retrieves and prints out dex entry
find_missing: finds and returns next missing entry in pokedex
print_dex: formatting the pokedex entries for output
print_dexfile: prints pokedex to Pokedex.txt
sort_dex: sorts the pokedex dictionary by putting keys(Dex numbers) in a sorted list and assigning old dictionary items in order by key. returns new dictionary
menu: prints ui menu. returns user answer
'''
def new_entry():
	'''
	Create a Pokemon object with base criteria, species, type, number
	'''
	name = (input("What is this Pokemon's name? ")).capitalize()
	type1 = (input("What is the primary type of this Pokemon? ")).capitalize()
	while type1 not in Types:
		type1 = (input("Sorry, that is not a known Pokemon type. Please enter a known type:\n>")).capitalize()

	result = input("Does this Pokemon have a secondary type? (Y/N) ")
	if result in ('y','Y'):
		type2 = (input("What type? ")).capitalize()
		while type2 not in Types:
			type2 = (input("Sorry, that is not a known Pokemon type. Please enter a known type:\n>")).capitalize()
	else:
		type2 = "none"
	num = input("What number would you like to assign this Pokemon? ")
	while num.isdigit() == False:
		num = input("Sorry, you must enter a number:\n>")
	num = int(num)

	return Pokemon.Pokemon(name,type1,type2,num)

def print_dex(pok):
	'''
	Outputs a single dex entry
	'''
	print("_______________________\n")
	print(pok.DexNum)
	print(pok.species)
	if pok.type2 != 'none':
		print(f"{pok.type1} {pok.type2}")
	else:
		print(pok.type1)
	print("_______________________")


def menu():
    print("Welcome! What would you like to do?")
    print("1: Record newly discovered Pokemon")
    print("2: Retrieve Pokemon Entry")
    print("3: Find Next Missing Pokemon")
    print("4: Print Pokedex to Screen")
    print("5: Update existing Pokemon entry")
    print("6: Exit")
    return int(input(">"))
def sort_dex(pokedex):
	#Sorts dictionary by creating list of the key value numbers and sorting, then reassigning to new dictionary
	Dexnums = list(pokedex.keys())
	Dexnums.sort()
	return {i: pokedex[i] for i in Dexnums}
def find_pok(pokedex):
	#prints pokemon to screen if found
	print("What Pokemon are you looking for?")
	pok = input("Dex Number or Species: ")
	if pok.isdigit():
	    pok = int(pok)
	else:
	    pok = pok.capitalize()
	    for p in pokedex:
		    if pok == pokedex[p].species:
			    pok = pokedex[p].DexNum
	try:
	    print_dex(pokedex[pok])
	except:
		print(f"Sorry, {pok} has not been recorded in this Pokedex.\n")
def edit_entry(pokedex):
	#edits the pokedex entry
	print("What Pokemon are you looking for?")
	pok = input("Dex Number or Species: ")
	if pok.isdigit():
	    pok = int(pok)
	else:
	    pok = pok.capitalize()
	    for p in pokedex:
		    if pok == pokedex[p].species:
			    pok = pokedex[p].DexNum
	try:
	   	print_dex(pokedex[pok])
	except:
		print(f"Sorry, {pok} has not been recorded in this Pokedex.\n")
		return 0
	print("What would you like to change?")
	print("1: Species")
	print("2: Types")
	print("3: Dex Number")
	#print("4: Height")
	#print("5: Weight")
	print("6: Exit")
	answer = int(input(">"))
	while answer not in (1,2,3,4,5,6):
		answer = input("Not an accepted option, please make another selection\n>")
	if answer == 1:
		print("What should the Species be?")
		pokedex[pok].setSpecies((input(">")).capitalize())
	if answer == 2:
		print("What type is this Pokemon?")
		type1 = (input(">")).capitalize()
		ans = input("Does this Pokemon have a secondary type? (Y/N)\n>")
		if ans in ("Y","y"):
			type2 = (input("What type?\n>")).capitalize()
		else:
			type2 = 'none'
		pokedex[pok].setType(type1,type2)

	if answer == 3:
		pokedex[pok].setDexNum(int(input("What number should this Pokemon be assigned to?\n>")))
		#reassign key value
		newMon = pokedex[pok]
		del pokedex[pok]
		pokedex[newMon.DexNum] = newMon
		sort_dex(pokedex)

def find_missing(pokedex):
	#returns next missing entry in dictionary
	for p in pokedex:
		try:
			pokedex[pokedex[p].DexNum + 1]
		except:
			return pokedex[p].DexNum + 1
		



def print_dexfile(pokedex):
	#prints dictionary to file
	#this feature will be unused when SQL is integrated
	dexfile = open('Pokedex.txt', mode = 'w')
	for pok in pokedex:
	    dexfile.write("_______________________\n")
	    dexfile.write(str(pokedex[pok].DexNum) + '\n')
	    dexfile.write(pokedex[pok].species + '\n')
	    if pokedex[pok].type2 != 'none':
		    dexfile.write(f"{pokedex[pok].type1} {pokedex[pok].type2}\n")
	    else:
		    dexfile.write(pokedex[pok].type1 + '\n')
	    dexfile.write("_______________________\n")
	dexfile.close()
	print("Pokedex Printed to File")

def retrieve_dex(pokedex):
	#retrieves saved pokedex and formats it to Pokemon objects
	try:
		dexfile = open('Pokedex.txt', mode = 'r')
	except:
		return 0
	dexlist = dexfile.readlines()
	dexfile.close()
	DexNum = 0
	spec = ""
	type1 = ""
	type2 = ""
	index = 0
	while index < len(dexlist):
		dexlist[index] = dexlist[index].strip()
		charindex = 0
		if dexlist[index].isdigit():
			DexNum = int(dexlist[index])
			index+=1
		elif dexlist[index] == '_______________________':
			index+=1
		else:	
			while charindex < len(dexlist[index]):
			    if dexlist[index][charindex].isspace():
				    dexlist[index] = dexlist[index].split()
			    charindex+=1

			if type(dexlist[index]) == list:
			    if dexlist[index][0] in Types:
			        type1 = dexlist[index][0]
			    if dexlist[index][1] in Types:
			        type2 = dexlist[index][1]
			    index+=1
			elif dexlist[index] in Types:
				type1 = dexlist[index]
				type2 = 'none'
				index+=1

			else:
				species = dexlist[index]
				index +=1
		if type1 and type2 and species != "" and DexNum > 0:
			pokedex[DexNum] = Pokemon.Pokemon(species,type1,type2,DexNum)
			type1 = ""
			type2 = ""
			species = ""
			DexNum = 0



'''
Main Processing

Pokedex retrieval
Menu manipulation
Pokedex Print to File

'''



pokedex = {}
retrieve_dex(pokedex)
answer = menu()
ans = ""
while answer != 6:
    if ans in ("n","N"):
        ans = ""
        answer = menu()
        if answer == 6:
        	break
    while answer not in (1,2,3,4,5,6):
        answer = input("Incorrect answer, please try again")
    if answer == 1:
        poke = new_entry()
        try:
            if pokedex[poke.DexNum].DexNum > 0:
        	    ans = input("Entry already exists at this number, would you like to overwrite it? (Y/N)\n>")
            if ans in ("n","N"):
                continue
        except:
        	pass
        pokedex[poke.DexNum] = poke
        pokedex = sort_dex(pokedex)
        con = 'y'
        while con in ('y','Y'):
            con = input("Would you like to enter another? (Y/N) ")
            if con in ('y','Y'):
                poke = new_entry()
                pokedex[poke.DexNum] = poke
                pokedex = sort_dex(pokedex)
    elif answer == 2:
	    find_pok(pokedex)
    elif answer == 3:
    	print(f"The next unrecorded Pokemon is at entry {find_missing(pokedex)}")
	
    elif answer == 4:
	    for p in pokedex:
		    print_dex(pokedex[p])
	    done = input("Enter anything when done\n>")
    elif answer == 5:
	    edit_entry(pokedex)
    answer = menu()
print_dexfile(pokedex)

