'''

Module for generating random stats and stuff for players. 

In particular, this class will be used to generate random players for the season. 

Players are assigned names, teams, a unique identifier, a position, and a skill level. 

'''

import math 
import random

NUM_FIRST_NAMES = 300
NUM_LAST_NAMES = 1000

class Player: 

  @staticmethod
  def Generate_Name(): 

    first = open("player_first_names.txt", "r")  
    last = open("player_last_names.txt", "r")

    fname = first.readlines()[random.randint(0, NUM_FIRST_NAMES)]
    lname = last.readlines()[random.randint(0, NUM_LAST_NAMES)]

    name = fname.strip() + " " + lname.strip()

    first.close() 
    last.close() 

    return name 


  def __init__(self): 
    self.id = 0 
    self.skill = 0 
    self.name = "" 
    self.Team = None 

  def get_skill(self): 
    return self.skill
  
  def set_skill(self, skill): 
    self.skill = skill
#EOF
