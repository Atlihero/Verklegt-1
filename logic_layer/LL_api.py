from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLTeams import LLTeams
from logic_layer.LLTournament import Tournament

class LL_API:
    def __init__(self):
        self.player = LLPlayer()
        self.team = LLTeams()
        self.tournament = Tournament()
    
    """
    The Logic layer wrapper for the LLPlayer
    """
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
    

    """
    Logic wrapper for Tournament
    """

    def get_contactInfo(self):
        "Gets the contact infro for the tournament contact"
        return self.tournament.get_contact_info()
    
    def update_contactInfo(self):
        "updates the info for the contact"
        return self.tournament.update_contact_info()
    
    def register_team(self):
        "registers the team to the tournament"
        return self.tournament.register_team()
    
    def scheduleGames(self):
        "schedules games for the tournament"
        return self.tournament.schedule_games()
    
    def recordResults(self):
        "records the info from a game and declares the winner"
        return self.tournament.record_result()
    
    def sum_Logic(self):
        "Idont know what this does"
        return self.tournament.sum_logic()
    
    def brackets(self):
        "sets the brackets of the tournament"
        return self.tournament.brackets_of_tournament()
    
    def Round(self):
        "the round for the tournament"
        return self.tournament.play_round()

