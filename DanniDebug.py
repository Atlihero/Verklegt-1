import csv

userinput = int(input("Select player ID: "))
PLAYER_PATH: str = r"data_layer\_data\Players.csv"

#Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
class PlayerIO:

    def get_players():
            players = []
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines()
                for row in reader:
                    players.append(row)
            return players
players = PlayerIO.get_players()
print(players[userinput])