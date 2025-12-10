from data_layer.PlayerIO import PlayerIO
from .LLTeams import LLTeams
from data_layer.data_api import DataAPI

class LLCaptain():
    
    MAX_TEAM_MEMBERS = 5

    def __init__(self):
        self.ll_teams = LLTeams()
        self.playerio = PlayerIO()
        self.dapi = DataAPI()


    def get_team_members(self, team_name: str) -> list:
        '''Check if players are in this team and return a list of members'''
        all_players = self.dapi.get_all_players()
        team_members = [] 
        for p in all_players:
            if p.get("Team") == team_name.strip():
                team_members.append(p)
        return team_members
            
    
    def get_available_players(self, team_name: str) -> list:
        '''Return availale players as a list if they are not a member of any team'''
        all_players = self.dapi.get_all_players()
        available_players = []
        for p in all_players:
    # if p.get("Team") is nothing or if p.get("Team").strip() are empty then it appends to the list
            if p.get("Team") is None or p.get("Team").strip() == "":
                available_players.append(p)


    def add_player_to_team(self, team_name: str, player_name: str):
        '''Used to check if team already has 5 players, '''
        team = self.ll_teams.get_team_by_name(team_name)
        if team is None:
            raise ValueError("Team not found")
        
        team_players = self.get_team_members(team_name)
        # Check if there are 5 people in team
        if len(team_players) > self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       
        # Get all players and find the player to add from a list
        all_players = self.playerio.get_players()
        player_to_add = None
        for p in all_players:
            if p.get("Name") == player_name:
                player_to_add = p
                break

        if player_to_add is None: # Check if empty
            raise ValueError("Player not found.")

        # Check if the player is already in a team
        if player_to_add.get("Team") not in (None, "", team_name):
            raise ValueError(f"{player_name} is already in another team.")

        # If player not in any team then we add him to our team
        player_to_add.get("Team") == team_name

        # Update players.csv and save the changes
        self.playerio.save_players(all_players)
        return player_to_add
    
    
    def remove_from_team(self, player_name: str, team_name: str):
        '''Allows captain to remove a player from team'''
        
        # Get all players and find the player to add from a list
        all_players = self.playerio.get_players()
        player_to_remove = None
        for p in all_players:
            if p.get("Name") == player_name:
                player_to_remove = p
                break
                    
        if player_to_remove is None:
            raise ValueError ("This player does not exist. Please try another player.")
        
        if player_to_remove.get("Team") != team_name:
            raise ValueError ("The player is not in this team. Please try another player.")
    
        player_to_remove.get("Team") == ""

        self.playerio.save_players(all_players)
        return player_to_remove
    

    def cap_see_player_info(self, team_name: str, player_name: str):
        '''Allows captains to see the players info that are on their team'''
        # Get the members in the team       
        team_players = self.get_team_members(team_name)
        for player in team_players:
            if player.get("Name") == player_name:
                return player
            #if player not found in the team
        raise ValueError("Player is not in this team. Please try another player.")
    
    