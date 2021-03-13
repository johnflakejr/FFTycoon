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

  #static value. increments each time a new player is generated
  id = 0

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

  @staticmethod
  def Generate_ID(): 
    Player.id = Player.id + 1
    return Player.id

  @staticmethod
  def Generate_Skill(): 
    id = id + 1
    return id

  def __init__(self,t): 
    #Make random skill level: 
    self.id = Player.Generate_ID()
    self.skill = random.randint(0, 100)
    #Type can be QB, WR, RB, TE, K, or DST
    self.type = t 
    self.name = Player.Generate_Name()
    self.Team = None 

  def get_skill(self): 
    return self.skill
  
  def set_skill(self, skill): 
    self.skill = skill

  def get_id(self):
    return self.id

  def get_name(self): 
    return self.name 

  def set_name(self,name): 
    self.name = name 

  def set_team(self, t): 
    self.team = t

  def get_team(self): 
    return self.team

  def get_type(self): 
    return self.type
  
  def __repr__(self): 
    out = self.name + ":\n"
    out = out + "Position: " + self.type + "\n"
    out = out + "Skill: " + str(self.skill) + "\n"
    return out
#EOF
