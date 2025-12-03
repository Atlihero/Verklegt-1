import csv

PLAYER_PATH: str = r"_data\Players.csv"
TEAM_PATH: str = r"_data\Teams.csv"

#Class for all the player info 
class PlayerIO:

    def get_players():
        players = [] #empty list for the player you are seeking
        with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile: 
            reader  = csvfile.readlines()
            for row in reader:
                players.append(row)
        return players

    def add_new_player(player: list):
        with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(player)
        return True

    def get_player_stats():
        "sækir tölfræði leikmanna"
        pass