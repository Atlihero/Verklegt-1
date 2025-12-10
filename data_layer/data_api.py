from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO
from data_layer.TournamentIO import TournamentIO

class DataAPI:
    def __init__(self):
        self.tournament = TournamentIO()
        self.player = PlayerIO()
        self.team = TeamIO()

    def get_all_Teams(self):
        "Gets all the teams an puts them in a list"
        return self.team.get_all_teams()

    def get_teams(self):
        "Gets the teams from the csv to the LL"
        return self.team.get_team()

    def get_all_players(self):
        "gets the players from the csv to the LL"
        return self.player.get_players()
    
    def public_get_player(self):
        "Gets the player for the public viewers"
        return self.player.get_player_PublicViewer()

    def add_team(self,team_dict):
        "adds a new team to the csv with the dict details"
        return self.team.add_new_team(team_dict)
    
    def getPublicTeam(self):
        "gets the teams for the public viewer"
        return self.team.getTeam_public()

    def add_player(self,player_dict):
        "adds a new player to the csv with the dict data"
        return self.player.create_new_player(player_dict)

    def get_team_statistics(self):
        "Retrieves team statistics"
        return self.team.get_team_stats()

    def get_player_statistics(self):
        "retrieves the player statistics"
        return self.player.get_player_stats()


    #Pæling að breyta þessum
    def add_team_to_tournament(self, tournament_name, teams_list):
        "add exactly 16 teams to the tournament"
        return self.team.add_teams_to_tournament(tournament_name, teams_list)

    def new_tournament(self, tournament_dict):
        "Creates a new tournament in the csv"
        return self.tournament.create_new_tournament(tournament_dict)

    def get_all_tournaments(self):
        "retrieves the tournaments from the csv"
        return self.tournament.get_tournaments()
    
    def get_tournamentNames(self):
        "retrieves the tournament names"
        return self.tournament.get_tournament_names()

# þessi þarf að vera 
    def create_new_tournaments(self, tournament_obj):
       return self.tournament.create_new_tournament(tournament_obj)

    def new_game(self, row: list):
        "creates a new game in the csv"
        return self.tournament.create_new_game(row)

    def get_games(self):
        "gets the games from the tournamnet"
        return self.tournament.get_all_games()
    
    def update_game(self, tournament_name: str, match_number: int, score_a: int, score_b: int):
        "updates the game based on the score inputted"
        return self.tournament.update_games(tournament_name, match_number, score_a, score_b)
    
    def advance_round(self, tournament_name: str, match_number: int, winner: str):
        return self.tournament.advance(tournament_name, match_number, winner)