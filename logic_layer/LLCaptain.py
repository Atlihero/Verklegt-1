from data_layer.PlayerIO import PlayerIO
from logic_layer.LLTeams import LLTeams

class LLCaptain():
    
    MAX_TEAM_MEMBERS = 5

    # def __init__(self, player_handler : LLPlayer, team_name: str, player_name: str):
    #     self.llplayerinfo = player_handler
    #     self.team_name = team_name
    #     self.player_name = player_name

    def __init__(self):
        self.ll_teams = LLTeams()
    # def __init__(self, player_handler : LLPlayer, team_name: str, player_name: str):
    #     self.llplayerinfo = player_handler
    #     self.team_name = team_name
    #     self.player_name = player_name

    def __init__(self):
        self.ll_teams = LLTeams()

    def get_team_members(self, team_name: str):
        '''Check if players are in this team and return a list of members'''
        all_players = PlayerIO.get_players()

        team_players = []
        for p in all_players:
            if p.team == team_name:
                team_players.append(p)
        return team_players
            
    def add_player_to_team(self, team_name: str, player_name: str):
        '''Used to check if team already has 5 players, '''
        team_players = self.get_team_members(team_name)

        # check if there are 5 people in team
        if len(team_players) > self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       
        # check if player is already in a team
        team_players = self.get_team_members(team_name)

        # check if there are 5 people in team
        if len(team_players) > self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       
        # check if player is already in a team
        all_players = PlayerIO.get_players()
        for p in all_players:
            if all_players == player_name:
                if p.team != "":
                    raise ValueError(f"{player_name} is already in another team. Please add another player to your team.")
                break

        added_player =  self.ll_teams.add_player_to_team(team_name, player_name)
        return added_player
    
    
    def remove_from_team(self, player_name: str, team_name: str):
        '''Allows captain to remove a player from team'''
        all_players = PlayerIO.get_players()
        player_found = None
        for p in all_players:
                if p.name == player_name:
                    player_found = p
                    break
                    
        if player_found is None:
            raise ValueError ("This player does not exist. Please try another player.")
        
        if player_found.team != team_name:
            raise ValueError ("The player is not in this team. Please try another player.")
    

    def cap_see_player_info(self, team_name: str, player_name: str):
        '''Allows the captain of each team to see his players information'''
        team_players = self.get_team_members(team_name)
        for player in team_players:
            if player.name == player_name:
                return player
        
        #if player not found
        raise ValueError("Player is not in this team. Please try another player.")
        

    def organizer_player_info(self):
        '''Allows the organizer to see all the players information'''
        all_players = PlayerIO.get_players()
        return all_players

        
        