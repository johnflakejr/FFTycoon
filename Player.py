'''

Module for generating random stats and stuff for players. 

In particular, this class will be used to generate random players for the season. 

Players are assigned names, teams, a unique identifier, a position, and a skill level. 

'''


import math 
import random

class Player: 


	def init(self): 
		self.id = 0 
		self.skill = 0 
		self.name = "" 
		self.Team = None 







	#Input: none, output: First and last name
	def generate_name(self): 

		first = open("player_first_names.txt","r")  
		last = open("player_last_names.txt","r")

		fname = first.readlines()[random.randint(0,300)]
		lname = last.readlines()[random.randint(0,1000)]

		name = fname.strip() + " " + lname.strip()

		first.close(); 
		last.close(); 

		return name; 
		



