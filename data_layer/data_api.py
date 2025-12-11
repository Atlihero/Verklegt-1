from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO
from data_layer.TournamentIO import TournamentIO

class DataAPI:
    def __init__(self):
        self.tournament = TournamentIO()
        self.player = PlayerIO()
        self.team = TeamIO()


    '''Data wrapper for PlayerIO'''

    def add_player(self,player_dict):
        '''Ads a new player to the csv with the dict data'''
        return self.player.create_new_player(player_dict)

    def get_all_players(self):
        '''Gets the players from the csv to the LL'''
        return self.player.get_players()

    def public_get_player(self):
        '''Gets the player for the public viewers'''
        return self.player.get_player_PublicViewer()


    '''Data wrapper for TeamIO'''

    def get_all_teams(self):
        '''Gets all the teams an puts them in a list'''
        return self.team.get_all_teams()

    def get_teams(self):
        '''Gets the teams from the csv to the LL'''
        return self.team.get_team()

    def add_team(self, name: str, captain: str, asciiLogo: str):
        '''Adds a new team to the csv with the dict details'''
        return self.team.create_new_team(name, captain, asciiLogo)
    
    def get_public_team(self):
        '''Gets the teams for the public viewer'''
        return self.team.get_team_public()

    def add_team_to_tournament(self, tournament_name, teams_list):
        '''Add exactly 16 teams to the tournament'''
        return self.team.add_teams_to_tournament(tournament_name, teams_list)


    '''Data wrapper for TournamentIO'''

    def new_tournament(self, tournament_dict):
        '''Creates a new tournament in the csv'''
        return self.tournament.create_new_tournament(tournament_dict)

    def get_all_tournaments(self):
        '''Retrieves the tournaments from the csv'''
        return self.tournament.get_tournaments()
    
    def get_tournamentNames(self):
        '''Retrieves the tournament names'''
        return self.tournament.get_tournament_names()

    def create_new_tournaments(self, tournament_obj):
        '''Creates new tournament and adds to csv file'''
        return self.tournament.create_new_tournament(tournament_obj)

    def new_game(self, row: list):
        '''Creates a new game in the csv'''
        return self.tournament.create_new_game(row)

    def get_games(self):
        '''Gets the games from the tournamnet'''
        return self.tournament.get_all_games()
    
    def update_game(self, tournament_name: str, match_number: int, score_a: int, score_b: int):
        '''Updates the game based on the score inputted'''
        return self.tournament.update_games(tournament_name, match_number, score_a, score_b)
    
    def advance_round(self, tournament_name: str, match_number: int, winner: str):
        '''Shows what team advances to the next round'''
        return self.tournament.advance(tournament_name, match_number, winner)
