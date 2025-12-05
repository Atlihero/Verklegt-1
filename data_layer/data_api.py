from PlayerIO import PlayerIO
from TeamIO import TeamIO
from TournamentIO import TournamentIO

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

    def add_team(self,team_dict):
        "adds a new team to the csv with the dict details"
        return self.team.add_new_team(team_dict)

    def add_player(self,player_dict):
        "adds a new player to the csv with the dict data"
        return self.add_player(player_dict)

    def get_team_statistics(self):
        "Retrieves team statistics"
        return self.get_team_statistics()

    def get_player_statistics(self):
        "retrieves the player statistics"
        return self.get_player_statistics()


    #Pæling að breyta þessum
    def add_teams_to_tournament(self, tournament_name, teams_list):
        "add exactly 16 teams to the tournament"
        return self.add_teams_to_tournament(tournament_name, teams_list)

    def new_tournament(self):
        "Creates a new tournament in the csv"
        return self.new_tournament

    def get_all_tournaments(self):
        "retrieves the tournaments from the csv"
        return self.get_all_tournaments()

    def new_game(self):
        "creates a new game in the csv"
        return self.new_game()
