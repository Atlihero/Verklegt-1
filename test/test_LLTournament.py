from logic_layer.LLTournament import TournamentService
from data_layer.TeamIO import TeamIO
from data_layer.PlayerIO import PlayerIO

team_io = TeamIO()
player_io = PlayerIO()
service = TournamentService(team_io, player_io)

print("Test OK, TournamentService created")



# test_LLTournament.py

from logic_layer.LLTournament import Tournament

def main():
    # create a tournament instance
    t = Tournament("Debug Tournament")

    # call one method just to see it works
    result = t.sum_logic("Team1")
    print("sum_logic('Team1') returned:", result)

if __name__ == "__main__":
    main()
