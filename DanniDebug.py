import csv


while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. add_new_player")

    val = input("Veldu verkefni (1-9): ")


    #Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
    PLAYER_PATH: str = r"data_layer\_data\Players.csv"

    
    if val == "1":
        userinput = int(input("Select player ID: "))
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

    if val == "2":
        class PlayerIO:
                def add_new_player(player):
                    with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)