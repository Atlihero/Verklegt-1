from PlayerIO import PlayerIO
from TeamIO import TeamIO

def get_all_teams():
    return TeamIO.get_team()

def get_all_players():
    return PlayerIO.get_players()

def add_team(team_dict):
    return TeamIO.create_new_team(team_dict)

def add_player(player_dict):
    return PlayerIO.create_new_player(player_dict)

def get_team_statistics():
    return TeamIO.get_team_stats()

def get_player_statistics():
    return PlayerIO.get_player_stats()

def add_teams_to_tournament(tournament_name, teams_list):
    return TeamIO.add_teams_to_tournament(tournament_name, teams_list)
