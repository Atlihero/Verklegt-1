from Models.Team import Team
from Models.Player import Player
from data_layer.TeamIO import TeamIO
from data_layer.PlayerIO import PlayerIO


class LLTeams:
    def __init__(self): 
        self.teams: list[Team] = self._load_teams_from_csv()

    
    def _load_teams_from_csv(self) -> list[Team]:
        raw_rows = TeamIO.get_team(self)
        teams: list[Team] = []

        for line in raw_rows: # Loops each line from the csv
            line = line.strip()
            if not line or line.startswith("TeamID"):
                continue # skip empty lines and header

            # splits on the comma and strips space + "
            parts = [p.strip(' "') for p in line.split(",")]

            # We need: TeamID, TeamName, Captain, wins, points
            if len(parts) < 5:
                continue

            teams.append(
                Team(
                    name=parts[1],       	
                    captain=parts[2],    	
                    asciiLogo="",
                    wins = int(parts[3]),	
                    points = int(parts[4])	
                )
            )

        return teams

    # per se þurfum ekki þetta fall, erum með í LLcaptain sem tékkar líka á fjölda í liði
    '''def add_player_to_team(self, team_name: str, player_name: str) -> Player:
        Captain wants to add a player to his team

        # Check if team exists
        team = self.get_team_by_name(team_name)
        if team is None:
            raise ValueError("A team with this name was not found.")

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
            raise ValueError("Player with this name was not found.")

        if player_to_add.team == team.name:
            raise ValueError("Player is already in this team.")

        # Update Players team
        player_to_add.team = team.name

        # Save player list through PlayerIO
        PlayerIO.save_players(players)

        return player_to_add'''

    
    def get_team_by_name(self, name: str) -> Team | None:
        '''Checks for the team and returns it if found, or None if not'''
        for team in self.teams:
            if team.name == name:
                return team
        return None

    
    def team_exists(self, name: str) -> bool:
        return self.get_team_by_name(name) is not None  # Checks if a team has this name

    
    def create_team(self, name: str, captain: str, asciiLogo: str) -> Team:
        '''Organizer wants to create a team'''
        # Checks whether it has a name, captain and a unique name
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

        # Saving in CSV through TeamIO
        row_for_csv = [
            str(new_id),
            new_team.name,
            new_team.captain,
            new_team.wins,
            new_team.points
        ]
        TeamIO.add_new_team(row_for_csv)

        return new_team

    
    def select_captain(self, team_name: str, new_captain: str) -> Team:
		'''Organizer wants to add a captain to a team.'''

        team = self.get_team_by_name(team_name)
		if team is None:
			raise ValueError("A team with this name was not found. Please make sure you have added the team before choosing a captain.")
		if not new_captain.strip():
			raise ValueError("Captain spot may not be empty. Please make sure that there is a captain for the team.")
		
		team.captain = new_captain.strip()

		return team

    
    def view_teams(self) -> list[Team]:
		'''User wants to see information about teams in the tournament.'''
        return list(self.teams)
