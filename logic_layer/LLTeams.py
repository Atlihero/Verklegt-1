from Models.Team import Team
from Models.Player import Player
from data_layer.TeamIO import TeamIO
from data_layer.PlayerIO import PlayerIO
from data_layer.data_api import DataAPI

api = DataAPI()


class LLTeams:
    def __init__(self): 
        self.teams: list[Team] = self._load_teams_from_csv()

    def getTeamsPublic(self):
        data = DataAPI()
        return data.getPublicTeam()

    def _load_teams_from_csv(self) -> list[Team]:
        raw_rows = TeamIO.get_team()
        teams: list[Team] = []

        for line in raw_rows:  # Loops each line from the csv
            line = line.strip()
            if not line or line.startswith("TeamID"):
                continue  # skip empty lines and header

            # Split á kommu og hreinsa bil + "
            parts = [p.strip(' "') for p in line.split(",")]

            # We need: TeamID, TeamName, Captain, wins, points
            if len(parts) < 5:
                continue

            teams.append(
                Team(
                    name=parts[1],       	
                    captain=parts[2],    	
                    asciiLogo="",        	# Logo for later
                    wins = int(parts[3]),	
                    points = int(parts[4])	
                )
            )

        return teams

    def add_player_to_team(self, team_name: str, player_name: str) -> Player:
        "Captain wants to add a player to his team"

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

        return player_to_add

    def get_team_by_name(self, name: str) -> Team | None:
        """Checks for the team and returns it if found, or None if not"""
        for team in self.teams:
            if team.name == name:
                return team
        return None

    def team_exists(self, name: str) -> bool:
        return self.get_team_by_name(name) is not None  # Checks if a team has this name

    def new_team(self, name: str, captain: str = None, asciiLogo: str = "") -> Team:
        new_team = Team(name=name, captain=captain, asciiLogo=asciiLogo)
        self.teams.append(new_team)

        DataAPI().add_team(name, captain, asciiLogo)

        return new_team

    def select_captain(self, team_name: str, new_captain: str) -> Team:
        "Organizer wants to chose a captain"

        team = self.get_team_by_name(team_name)
        if team is None:
            raise ValueError("Team with this name was not found")
        if not new_captain.strip():
            raise ValueError("The captain can not be empty")

        team.captain = new_captain.strip()

        return team

    def view_teams(self) -> list[Team]:
        "Spectator wants to see information about a team"
        return list(self.teams)
