from Models.Team  import Team
from data_layer import TeamIO
from data_layer import PlayerIO

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

		# If it has less than 2 parts then we skip it instead of crashing
			if len(parts) < 2:
					continue  

			name = parts[0]
			captain = parts[1]
			asciiLogo = parts[2] if len(parts) > 2 else "" # Third field is the logo or "" if it does not exist

			team = Team(name=name, captain=captain, asciiLogo=asciiLogo)
			teams.append(team)

		return teams
		
	

	def add_player(self, team_name: str, player_id: str):
		"Fyrirliði vill bæta leikmanni í lið"

		# Check if team exists
		team = self.get_team_by_name(team_name)
		if team is None:
				raise ValueError("A team with this name was not found.")
		
		# Get all players from data layer
		players = PlayerIO.get_players()

		# Find player with the right ID
		player_to_add = None
		for p in players:
			if p.id == player_id:
				player_to_add = p
				break

		# Check if player is already in this team
		if player_to_add is None:
			raise ValueError("Player with this ID was not found.")
		
		if player_to_add.team == team.name:
			raise ValueError("Leikmaður er nú þegar í þessu liði.")
		
		# Update Players team
		player_to_add.team = team.name

		# Save player list through PlayerIO
		PlayerIO.save_players(players)  

		return player_to_add
		
	def get_team_by_name(self, name: str): # Checks for the teama and returns it if found, or None if not
		for team in self.teams:
			if team.name == name:
				return team
		return None     

	def team_exists(self, name: str):
		return self.get_team_by_name(name) is not None  # Checks if a team has this name

	def create_team(self, name: str, captain: str, asciiLogo: str):
		"skipuleggjandi vill búa til lið"
		# Checks weather it has a name, captain and a unique name
		if not name.strip():
			raise ValueError("Name can not be empty")
		if not captain.strip():
			raise ValueError("Captain can not be empty")
		if self.team_exists(name):
			raise ValueError("Another team already has this name")
		
		# Creating team object
		new_team = Team(name=name.strip(), captain=captain.strip(), asciiLogo=asciiLogo)

		# Updating in memory
		self.teams.append(new_team)

		# Saving in CSV throguh TeamIO
		row_for_csv = [new_team.name, new_team.captain, new_team.asciiLogo, 0, 0] # 0 wins & 0 points to begin with
		TeamIO.add_new_team(row_for_csv)

		return new_team

	def select_captain(self, team_name: str, new_captain: str):
		"Skipuleggjandi vill velja fyriliða í liði"

		team = self.get_team_by_name(team_name)
		if team is None:
			raise ValueError("Team with this name was not found")
		if not new_captain.strip():
			raise ValueError("The captain can not be empty")
		
		team.captain = new_captain.strip()

		return team

	def view_teams(self):
		"áhorfandi vill skoða upplýsingar liða"
		return list(self.teams)


player = LLTeams.add_player()
player