from logic_layer.LLTournament import TournamentService
from data_layer.TeamIO import TeamIO
from data_layer.PlayerIO import PlayerIO

team_io = TeamIO()
player_io = PlayerIO()
service = TournamentService(team_io, player_io)

print("Test OK, TournamentService created")



