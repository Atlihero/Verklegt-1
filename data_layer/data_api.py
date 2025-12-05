from PlayerIO import PlayerIO
from TeamIO import TeamIO
from TournamentIO import TournamentIO

class DataAPI:
    def __init__(self):
        self.tournament = TournamentIO()
        self.player = PlayerIO()
        self.team = TeamIO()

def get_all_Teams(team_list):
    "Gets all the teams an puts them in a lsit"
    return TeamIO.get_all_teams(team_list)

def get_teams():
    "Gets the teams from the csv to the LL"
    return TeamIO.get_team()

def get_all_players():
    "gets the players from the csv to the LL"
    return PlayerIO.get_players()

def add_team(team_dict):
    "adds a new team to the csv with the dict details"
    return TeamIO.create_new_team(team_dict)

def add_player(player_dict):
    "adds a new player to the csv with the dict data"
    return PlayerIO.create_new_player(player_dict)

def get_team_statistics():
    "Retrieves team statistics"
    return TeamIO.get_team_stats()

def get_player_statistics():
    "retrieves the player statistics"
    return PlayerIO.get_player_stats()


#Pæling að breyta þessum
def add_teams_to_tournament(tournament_name, teams_list):
    "add exactly 16 teams to the tournament"
    return TeamIO.add_teams_to_tournament(tournament_name, teams_list)

def new_tournament():
    "Creates a new tournament in the csv"
    return TournamentIO.create_new_tournament()

def get_all_tournaments():
    "retrieves the tournaments from the csv"
    return TournamentIO.get_tournaments()

def new_game():
    "creates a new game in the csv"
    return TournamentIO.create_new_game()