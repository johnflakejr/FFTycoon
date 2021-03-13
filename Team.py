"""
  Class for teams. 

  There will be 32 teams.  Each will have: 
  1. A roster
  2. A "Power Ranking" based on the cumulative skill of the players
"""

class Team: 

  possible_names = []
  
  @staticmethod
  def Generate_Name():
    return possible_names.pop()

  @staticmethod
  def Load_Team_Names(name_file): 
    nf = open(name_file, "r")
    for line in nf: 
      possible_names.append(line)
    nf.close()
  

  def __init__():
    self.name = Generate_Name()
    self.roster = []

  def get_name(self): 
    return self.name

  def add_player(self, player):
    self.roster.append(player); 

  def cut_player(self, player_name): 
    pass

  def get_roster(self): 
    return self.roster

'''
  def __init__(self,teamName): 

		self.teamName = teamName
		self.roster = {} 
		self.generate_team()

	def generate_team(self): 

		#Make Player.Players: 
		qb1 = Player.Player("QB") 
		self.roster["QB1"] = qb1
		qb2 = Player.Player("QB") 
		self.roster["QB2"] = qb2
		wr1 = Player.Player("WR") 
		self.roster["WR1"] = wr1
		wr2 = Player.Player("WR") 
		self.roster["WR2"] = wr2
		wr3 = Player.Player("WR") 
		self.roster["WR3"] = wr3
		wr4 = Player.Player("WR") 
		self.roster["WR4"] = wr4
		wr5 = Player.Player("WR") 
		self.roster["WR5"] = wr5
		rb1 = Player.Player("RB") 
		self.roster["RB1"] = rb1
		rb2 = Player.Player("RB") 
		self.roster["RB2"] = rb2
		rb3 = Player.Player("RB") 
		self.roster["RB3"] = rb3
		te1 = Player.Player("TE") 
		self.roster["TE1"] = te1
		te2 = Player.Player("TE") 
		self.roster["TE2"] = te2
		k = Player.Player("K") 
		self.roster["K"] = k
		dst = Player.Player("DST")
		self.roster["DST"] = dst
		dst.set_name(self.teamName + " D/ST"); 


	def __repr__(self): 
		out = "Team: " + self.teamName + "\n"
		out = out + "Roster: " + "\n"
		out = out + "QB1: " + str(self.roster["QB1"]); 
		out = out + "QB2: " + str(self.roster["QB2"]); 
		out = out + "WR1: " + str(self.roster["WR1"]); 
		out = out + "WR2: " + str(self.roster["WR2"]); 
		out = out + "WR3: " + str(self.roster["WR3"]); 
		out = out + "WR4: " + str(self.roster["WR4"]); 
		out = out + "WR5: " + str(self.roster["WR5"]); 
		out = out + "RB1: " + str(self.roster["RB1"]); 
		out = out + "RB2: " + str(self.roster["RB2"]); 
		out = out + "RB3: " + str(self.roster["RB3"]); 
		out = out + "TE1: " + str(self.roster["TE1"]); 
		out = out + "TE2: " + str(self.roster["TE2"]); 
		out = out + "K: " + str(self.roster["K"]); 
		out = out + "D/ST: " + str(self.roster["DST"]); 
		return out; 
		
		
'''
#EOF
