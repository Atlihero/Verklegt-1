import csv


while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. add_new_player")
    print("3. get team")
    print("4. get player stats")

    val = input("Veldu verkefni (1-4): ")


    #Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
    PLAYER_PATH: str = r"data_layer\_data\Players.csv"
    TEAM_PATH: str = r"data_layer\_data\Teams.csv"

    
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
                def add_new_player(player: list):
                    with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(player)
                    return True

    if val == "3":
        userinput = int(input("Veldu lið á milli 1-18: "))
        class TeamIO:
             def get_team():
                Teams = []
                with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                    reader  = csvfile.readlines()
                    for row in reader:
                        Teams.append(row)
                return Teams
        Teams = TeamIO.get_team()
        print(Teams[userinput])

    if val == "4":
        userinput = int(input("Sláðu inn ID leikmanns sem þú vilt skoða: "))
        class PlayerIO:
            def get_player_stats():
                    Points = []
                    with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            Points.append(row["Points"])
                    return Points
        Points = PlayerIO.get_player_stats()
        print(Points[userinput])
