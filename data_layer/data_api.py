from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO
from data_layer.TournamentIO import TournamentIO
from Models.Player import Player

class DataAPI:
    def __init__(self):
        self.tournament = TournamentIO()
        self.player = PlayerIO()
        self.team = TeamIO()


    '''Data wrapper for PlayerIO'''

    def get_all_players(self) -> list:
        '''Gets the players from the csv and ready for the logic layer'''
        return self.player.get_players()

    def public_get_player(self) -> list:
        '''Gets the player for the public viewers'''
        return self.player.get_player_public_viewer()
    
    def save_new_player(self, players: list[Player]) -> None:
        '''Saves a player in the csv file with all needed information'''
        return self.player.save_players(players)
    
    def add_player(self,player_dict: list) -> str:
        '''Adds a new player to the csv file'''
        return self.player.create_new_player(player_dict)


    '''Data wrapper for TeamIO'''

    def get_teams(self) -> list:
        '''Gets the teams from the csv and ready for the logic layer'''
        return self.team.get_team()
    
    def get_public_team(self) -> list:
        '''Gets the teams for the public viewer'''
        return self.team.get_team_public()
    
    def add_team(self, name: str, captain: str, asciiLogo: str) -> str:
        '''Adds a new team to the csv file'''
        return self.team.create_new_team(name, captain, asciiLogo)
    
    def add_team_to_tournament(self, tournament_name: str, teams_list: list) -> str:
        '''Add teams to the tournament'''
        return self.team.add_teams_to_tournament(tournament_name, teams_list)

    def get_all_teams(self) -> list:
        '''Gets all the teams and puts them in a list'''
        return self.team.get_all_teams()

    '''Data wrapper for TournamentIO'''

    def get_all_tournaments(self) -> list:
        '''Retrieves the tournaments from the csv file'''
        return self.tournament.get_tournaments()
    
    def get_tournament_names(self) -> list:
        '''Retrieves the tournament names'''
        return self.tournament.get_tournament_names()

    def create_new_tournaments(self, tournament_obj: list) -> str:
        '''Creates new tournament and adds to csv file'''
        return self.tournament.create_new_tournament(tournament_obj)

    def new_game(self, row: list) -> str:
        '''Creates a new game in the csv file'''
        return self.tournament.create_new_game(row)

    def get_games(self) -> list:
        '''Gets the games from the tournament'''
        return self.tournament.get_all_games()
    
    def update_game(self, tournament_name: str, match_number: int, score_a: int, score_b: int) -> str:
        '''Updates the game based on the inputted score'''
        return self.tournament.update_games(tournament_name, match_number, score_a, score_b)
    
    def advance_round(self, tournament_name: str, match_number: int, winner: str) -> str:
        '''Shows what team advances to the next round'''
        return self.tournament.advance(tournament_name, match_number, winner)
