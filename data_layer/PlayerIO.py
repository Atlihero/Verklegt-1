import csv

PLAYER_PATH: str = r"_data\Players.csv"

#Class for all the player info 
class PlayerIO:

    def add_new_player(player: list):
        with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(player)
        return True

    def get_player_stats():
        "sækir tölfræði leikmanna"
        pass