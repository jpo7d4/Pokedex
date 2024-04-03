'''
Pokemon Class
Object with species, two types, and a Dex number
Data items for stats to be used in AI project down the line
height and weight to be used when Pokedex project integrates SQL
Primarily contains setters for values
'''


class Pokemon():
	def __init__(self,species,type1,type2,DexNum):
		self.species = species
		self.type1 = type1
		self.type2 = type2
		self.DexNum = DexNum
		self.attack = 0
		self.spattack = 0
		self.defense = 0
		self.health = 0
		self.spdefense = 0
		self.speed = 0
		self.height = 0
		self.weight = 0

	def __str__(self):
		return f"This is {self.species}, a {self.type1} type Pokemon"

	def stats(self):
		if self.type2 == 'none':
			print(f"{self.species} is a {self.type1} Pokemon")
		else:
			print(f"{self.species} is a {self.type1}/{self.type2} Pokemon")
		if self.attack != 0:
			print(f"Your {self.species}'s stats:")
			print(f"Health: {self.health}\nAttack: {self.attack}\nSpecial Attack: {self.spattack}\nDefense: {self.defense}\nSpecial Defense: {self.spdefense}\nSpeed: {self.speed}")
	def setStats(self,health,attack,spattack,defense,spdefense,speed):
		self.health = health
		self.attack = attack
		self.spattack = spattack
		self.defense = defense
		self.spdefense = spdefense
		self.speed = speed
		print(self.attack)
	def setSpecies(self,species):
		self.species = species
	def setType(self,type1,type2):
		self.type1 = type1
		self.type2 = type2
	def setDexNum(self,DexNum):
		self.DexNum = DexNum

	def setHeightWeight(self, height, weight):
		if height > 0:
			self.height = height
		if weight > 0:
			self.weight = weight




