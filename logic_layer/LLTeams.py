from Models.Team import Team
from data_layer.TeamIO import TeamIO
from data_layer.PlayerIO import PlayerIO

class LLTeams:

	def __init__(self):
		self.teams: list[Team] = self._load_teams_from_csv()


	def _load_teams_from_csv(self):
		raw_rows = TeamIO.get_team()
		teams: list[Team] = []

		for line in raw_rows:   # Loops each line from the csv
			line = line.strip()
			if not line:    # Skip if line is empty
				continue
			# Spliting on the comma and loops each field
			parts = [p.strip().strip('"') for p in line.split(",")]

			if parts[0] == "TeamID": # skip the header
				continue
		
			# If it has less than 3 parts then we skip it instead of crashing
			if len(parts) < 3:
				continue  

			name = parts[1]
			captain = parts[2]
			asciiLogo = ""

			team = Team(name, captain, asciiLogo)
			teams.append(team)

		return teams


	def add_player_to_team(self, team_name: str, player_name: str):
		'''Captain wants to add a player to his team.'''

		# Check if team exists
		team = self.get_team_by_name(team_name)
		if team is None:
			raise ValueError("A team with this name was not found. Please make sure a team exists before adding to team.")
		
		# Get all players from data layer
		players = PlayerIO.get_players()

		# Find player with the right name
		player_to_add = None
		for p in players:
			if p.name == player_name:
				player_to_add = p
				break

		# Check if player is already in this team
		if player_to_add is None:
			raise ValueError("Player with this name was not found. Please use another name.")
		
		if player_to_add.team == team.name:
			raise ValueError("The player is already in this team. Please choose another player.")
		
		'''# bæta við að ef leikmaður er í öðru liði'''
		
		# Update Players team
		player_to_add.team = team.name

		# Save player list through PlayerIO
		PlayerIO.create_new_player(players)  

		return player_to_add


	def get_team_by_name(self, name: str): 
		'''Checks for the teama and returns it if found, or None if not'''
		for team in self.teams:
			if team.name == name:
				return team
		return None


	def team_exists(self, name: str):
		'''Checks if a team already has this name'''
		return self.get_team_by_name(name) is not None  


	def create_team(self, name: str, captain: str, asciiLogo: str):
		'''Organizer wants to make a team'''
		# Checks weather it has a name, captain and a unique name
		if not name.strip():
			raise ValueError("Name can not be empty. Please enter a name.")
		if not captain.strip():
			raise ValueError("Captain can not be empty. Please enter a name.")
		if self.team_exists(name):
			raise ValueError("A team with this name already exists. Please use another name.")

		# Creating team object
		new_team = Team(name=name.strip(), captain=captain.strip(), asciiLogo=asciiLogo)

		# Updating in memory
		self.teams.append(new_team)
		new_id = len(self.teams)   

		# Saving in CSV throguh TeamIO
		# teams start with 0 wins and points
		row_for_csv = [str(new_id), new_team.name, new_team.captain, 0, 0]
		TeamIO.add_new_team(row_for_csv)

		return new_team
	

	def select_captain(self, team_name: str, new_captain: str): # -> Team
		'''Organizer wants to add a captain to a team.'''

		team = self.get_team_by_name(team_name)
		if team is None:
			raise ValueError("A team with this name was not found. Please make sure you have added the team before choosing a captain.")
		if not new_captain.strip():
			raise ValueError("Captain spot may not be empty. Please make sure that there is a captain for the team.")
		
		team.captain = new_captain.strip()

		return team


	def view_teams(self):
		'''User wants to see information about teams in the tournament.'''

		return list(self.teams)
