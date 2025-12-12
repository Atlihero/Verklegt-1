from Models.Team import Team
from Models.Player import Player
from data_layer.data_api import DataAPI


class LLTeams:
    def __init__(self): 
        self.data = DataAPI()

    
    def get_teams_public(self) -> list:
        '''The public viewer can see the teams.'''
        
        return self.data.get_public_team()

    
    def add_player_to_team(self, team_name: str, player_name: str) -> Player:
        '''Captain wants to add a player to his team'''
        
        # Check if team exists
        team = self.get_team_by_name(team_name)
        if team is None:
            raise ValueError("A team with this name was not found.")

        # Get all players from data layer
        players = self.data.get_all_players()

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

        # Save player list through the data layer
        self.data.save_new_player(players)


        return player_to_add

    
    def get_team_by_name(self, name: str) -> Team | None:
        '''Checks for the team and returns it, if it was found, or None if it was not found'''
        
        for team in self.teams:
            if team.name == name:
                return team
        return None

    
    def team_exists(self, name: str) -> bool:
        '''Checks if a team with the inputted name already exists.'''
        
        return self.get_team_by_name(name) is not None  # Check if a team has this name

    
    def new_team(self, name: str, captain: str = None, asciiLogo: str = "") -> Team:
        '''Create a new team and add it to the csv file.'''
        
        new_team = Team(name=name, captain=captain, asciiLogo=asciiLogo)
        
        # saves the new team in the data_layer
        self.data.add_team(name, captain, asciiLogo)

        return new_team

    
    def select_captain(self, team_name: str, new_captain: str) -> Team:
        '''Organizer wants to choose a captain'''
        
        team = self.get_team_by_name(team_name)
        if team is None:
            raise ValueError("No team with this name was not found. Please try again.")
        if not new_captain.strip():
            raise ValueError("The captain's name can not be empty. Please enter a captain name")

        team.captain = new_captain.strip()

        return team

    
    def view_teams(self) -> list[Team]:
        '''Spectator wants to see information about a team. Returns a list of all teams.'''
        
        return list(self.teams)
