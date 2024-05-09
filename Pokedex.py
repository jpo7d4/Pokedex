'''
Pokedex Project

Takes in data from Pokedex table on an Oracle SQL database
Program will take in user input to create more Pokemon objects.
That data can be altered based on user input
Oracle SQL table is created if it does not exist
Pokedex dictionary is then uploaded to Oracle SQL database via insert or update


'''


import Pokemon
import oracledb
global Types
global username
global pw
global path
#define db parameters here:
#user:
username = "user"
#password:
pw = "password"
#dsn:
path = "dsn"
Types = ['Grass','Fire','Water','Electric','Rock','Ground','Fighting','Psychic','Ghost','Poison','Bug','Ice','Dragon','Normal','Flying','Dark','Steel','Fairy']
'''
Function Descriptions:
new_entry: pulls user input to create new pokemon object. object then gets returned
update_entry: Lets user update a pre-existing pokedex entry
upload_dex: creates table if needed, and calls insert and update functions
update_dex: Updates existing records in Pokedex table
insert_dex: inserts new records to Pokedex table
download_dex: pulls records from Pokedex table and creates Pokedex dictionary
find_pok: retrieves and prints out dex entry
find_missing: finds and returns next missing entry in pokedex
print_dex: formatting the pokedex entries for output

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
	print(f'{pok.height} cm')
	print(f'{pok.weight} kg')
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
	print("4: Height")
	print("5: Weight")
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
	if answer == 4:
		ans = float(input('How tall is this Pokemon?\n>'))
		pokedex[pok].setHeightWeight(ans,0)
	if answer == 5:
		ans = float(input('How much does this Pokemon weigh?\n>'))
		pokedex[pok].setHeightWeight(0,ans)
		

def find_missing(pokedex):
	#returns next missing entry in dictionary
	for p in pokedex:
		try:
			pokedex[pokedex[p].DexNum + 1]
		except:
			return pokedex[p].DexNum + 1
		




def insert_dex(pok):
	#connects to database and inserts pokemon object to pokedex table
	connection = oracledb.connect(
		user = username,
		password = pw,
		dsn = path
		)
	cursor = connection.cursor()
	cursor.execute("""
		INSERT INTO Pokedex
		VALUES(:dexnum, :species, :type1, :type2, :weight, :height)

		""", (pok.DexNum, pok.species, pok.type1, pok.type2, pok.height, pok.weight))
	connection.commit()
	print(f"{pok.species} successfully recorded in Pokedex")

def update_dex(pok):
	#connects to database and updates pokemon data in pokedex table
	connection = oracledb.connect(
		user = username,
		password = pw,
		dsn = path
		)
	cursor = connection.cursor()
	cursor.execute("""
		UPDATE pokedex
		SET species = :species, type1 = :type1, type2 = :type2, weight = :weight, height = :height
		WHERE dexnum = :dexnum
		""", (pok.species,pok.type1,pok.type2,pok.weight,pok.height,pok.DexNum))
	connection.commit()
	cursor.execute("""
		UPDATE pokedex
		SET dexnum = :dexnum
		WHERE species = :species
		""",(pok.DexNum,pok.species))

	connection.commit()
	print(f"{pok.species} Pokedex entry updated.")

def upload_dex(pokedex):
	#connects to database and creates table if needed. insert_dex and update_dex are called from here
	connection = oracledb.connect(
		user = username,
		password = pw,
		dsn = path
		)
	cursor = connection.cursor()
	cursor.execute("""
    	begin
       		execute immediate 'drop table todoitem';
        	exception when others then if sqlcode <> -942 then raise; end if;
    	end;""")
	try:
		cursor.execute("""
			CREATE TABLE Pokedex(
				dexnum number not null,
				species varchar(50) not null,
				type1 varchar(50),
				type2 varchar(50),
				weight number(10,2),
				height number(10,2),

				CONSTRAINT pok_pk PRIMARY KEY (dexnum, species)
				)

			""")
	except:
		print("Saving Pokedex...\n")
	for pok in pokedex:
		try:
			cursor.execute("""SELECT * FROM Pokedex""")
			for dexnum, species, type1, type2, weight, height in cursor:
				if dexnum == pokedex[pok].DexNum or species == pokedex[pok].species:
					if dexnum != pokedex[pok].DexNum or species != pokedex[pok].species or type1 != pokedex[pok].type1 or type2 != pokedex[pok].type2 or weight != pokedex[pok].weight or height != pokedex[pok].height:
						try:
							update_dex(pokedex[pok])
						except:
							print(f'{pokedex[pok].species} update failed')
		except:
			insert_dex(pokedex[pok])
	print("Pokedex Saved!")


			
				
			


def download_dex(pokedex):
	#connects to database and creates new pokedex dictionary from data in pokedex table
	try:

		connection = oracledb.connect(
			user = username,
			password = pw,
			dsn = path
			)
		cursor = connection.cursor()
		cursor.execute("""SELECT * FROM Pokedex
			ORDER BY dexnum""")
		for dexnum, species, type1, type2, height, weight in cursor:
			pok = Pokemon.Pokemon(species, type1, type2, dexnum)
			pok.setHeightWeight(height,weight)
			pokedex[dexnum] = pok
		print('Pokedex downloaded...\n')
	except:
		print("Pokedex download failed or table not found. Pokedex table will be created.\n")






'''
Main Processing

Pokedex retrieval
Menu manipulation
Pokedex upload

'''



pokedex = {}
download_dex(pokedex)

answer = menu()
ans = ""
while answer != 6:
    if ans in ("n","N"):
        ans = ""
        answer = menu()
        if answer == 6:
        	break
    while answer not in (1,2,3,4,5,6):
        answer = int(input("Incorrect answer, please try again\n>"))
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
	    pokedex = sort_dex(pokedex)
    answer = menu()
upload_dex(pokedex)
