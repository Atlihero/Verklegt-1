from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLTeams import LLTeams

class LL_API:
    def __init__(self):
        self.player = LLPlayer()
        self.team = LLTeams()
    
    """
    The Logic layer wrapper for the LLPlayer
    """
    def getplayers(self):
        "gets player and his information"
        return self.player.get_all_players()
    
    def getPlayerPublic(self):
        "gets the player for the public viewers"
        return self.player.get_player_publicViewer()
    
    def getTeamPublic(self):
        "gets the teams for the public viewer"
        return self.team.get_team_public()
    
    def getPlayer_stats(self):
        "Get the stats of players"
        return self.player.get_player_statistics()

    def valid_dob(self, dob):
        "Validates players date of birth"
        return self.player.validate_dob(dob)
    
    def valid_phone(self, phone):
        "validates the phone number"
        return self.player.validate_phone(phone) 
    
    def valid_email(self, email):
        "Validates the email"
        return self.player.validate_email(email)
    
    def valid_handle(self, handle):
        "validates the handle of new players"
        return self.player.validate_handle(handle)
    
    def validate_link(self, link):
        "validates the link of the new players"
        return self.player.validate_link(link)
    
    def create_player(self, name, dob_string, phone, email, handle, link):
        "creates a new player"
        return self.player.create_player(name, dob_string, phone, email, handle, link)
    
    """
    Logic layer wrapper for the LLTeams
    """
    def load_team(self):
        "loads a team from the csv"
        return self.team._load_teams_from_csv()
    
    def add_player(self, team_name, player_name):
        "add player to team"
        return self.team.add_player_to_team(team_name, player_name)
    
    def get_teams(self, name):
        "gets the team by name"
        return self.team.get_team_by_name(name)
    
    def check_team(self, name):
        "Check if team has this name"
        return self.team.team_exists(name)

    def add_team(self, name, captain, asciiLogo):
        "creates a new team"
        return self.team.create_team(name, captain, asciiLogo)

    def select_captains(self, team_name, new_captain):
        "selects a new captain for a team"
        return self.team.select_captain(team_name, new_captain)

    def view_teams(self):
        "Public viewer wants to view teams"
        return self.team.view_teams() 

