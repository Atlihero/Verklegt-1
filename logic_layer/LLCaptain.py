from data_layer.PlayerIO import PlayerIO
from .LLTeams import LLTeams
from data_layer.data_api import DataAPI

class LLCaptain():
    
    MAX_TEAM_MEMBERS = 5

    def __init__(self):
        self.ll_teams = LLTeams()


    def get_team_members(self, team_name: str):
        '''Check if players are in this team and return a list of members'''
        all_players = DataAPI.get_all_players()
        team_members = [p for p in all_players if p.get("Team") == team_name]
        return team_members
            

    def add_player_to_team(self, team_name: str, player_name: str):
        '''Used to check if team already has 5 players, '''
        team = self.ll_teams.get_team_by_name(team_name)
        if team is None:
            raise ValueError("Team not found")
        
        team_players = self.get_team_members(team_name)
        # check if there are 5 people in team
        if len(team_players) > self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       
        # Get all players
        all_players = PlayerIO().get_players()

        # Find the player to add from a list
        player_to_add = None
        for p in all_players:
            if p.get("Name") == player_name:
                player_to_add = p
                break

        if player_to_add is None:
            raise ValueError("Player not found.")

        # have to check if player is already in a team
        if player_to_add.get("Team") not in (None, "", team_name):
            raise ValueError(f"{player_name} is already in another team.")

        # if player not in any team then we add to our team
        player_to_add.get("Team") == team_name

        # Update players.csv and save changes
        PlayerIO.save_players(all_players)
        return player_to_add
    
    
    def remove_from_team(self, player_name: str, team_name: str):
        '''Allows captain to remove a player from team'''
        all_players = PlayerIO.get_players()
        player_found = None

        for p in all_players:
            if p.get("Name") == player_name:
                player_found = p
                break
                    
        if player_found is None:
            raise ValueError ("This player does not exist. Please try another player.")
        
        if player_found.get("Team") != team_name:
            raise ValueError ("The player is not in this team. Please try another player.")
    
        player_found.get("Team") == ""

        PlayerIO.save_players(all_players)
        return player_found
    

    def cap_see_player_info(self, team_name: str, player_name: str):
        '''Allows captains to see the players info that are on their team'''
        team_players = self.get_team_members(team_name)
        for player in team_players:
            if player.get("Name") == player_name:
                return player
            #if player not found in the team
        raise ValueError("Player is not in this team. Please try another player.")
    
    