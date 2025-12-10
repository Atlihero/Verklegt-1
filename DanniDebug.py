import csv
from Models.Game import Game

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Create new player")
    print("3. Get team")
    print("4. Get player stats")
    print("5. Create new team")
    print("6. Get team stats")
    print("7. Get Tournament")
    print("8. Create Tournament")
    print("9. Get_games")
    print("10. Create new Game")

    val = input("Veldu verkefni (1-8): ")


    #Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
    PLAYER_PATH: str = r"data_layer\_data\Players.csv"
    TEAM_PATH: str = r"data_layer\_data\Teams.csv"
    TOURNAMENT_PATH: str = r"data_layer\_data\Tournament.csv"
    GAMES_PATH: str = r"data_layer\_data\Games.csv"

    
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
        name = input("Name: ")
        Dob = input("Date of birth (00/00/0000): ")
        Address = input("Address: ")
        Phone = input("Phonenumber: ")
        Email = input("Email: ")
        Handle = input("Choose a handle: ")

        team = "No Team"
        Points = 0

        player = [name, Dob, Address, Phone, Email, Handle, team, Points]

        class PlayerIO:
                def create_new_player(player: list):
                    try: 
                        with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(player)
                        return "Búin að búa til leikmann"
                    except ValueError:
                        return f"Villa kom upp :O"

        print(PlayerIO.create_new_player(player))

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
        userinput = int(input("Select the number of the player you want to check out: "))
        class PlayerIO:
            def get_player_stats():
                    Points = []
                    Handle = []
                    with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            Points.append(row["Points"])
                            Handle.append(row["Handle"])
                    return Handle, Points
        Handle, Points = PlayerIO.get_player_stats()
        print(Handle[userinput-1], Points[userinput-1], "Points")

    if val == "5":
        teamName = input("TeamName: ")
        captain = "No Captain"

        team = [teamName, captain]
         
        class TeamIO:
            def create_new_team(team: list):
                try: 
                    with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(team)
                    return f"New Team added :)"    
                except ValueError:
                    f"Error message to be decided"
        print(TeamIO.create_new_team(team))

    
    if val == "6":
        userinput = int(input("Sláðu inn númer liðs: "))
        class TeamIO:
            def get_team_stats():
                Team_name = []
                with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        Team_name.append(row["TeamName"])
                        Wins.append(row["Wins"])
                        Points.append(row["Points"])
                    return Team_name, Wins, Points
        Team_name, Wins, Points = TeamIO.get_team_stats() 
        print(f"{Team_name[userinput]}")

    
    if val == "7":
        userinput = int(input("Sláðu inn númer móts: "))
        class TournamentIO:
            def get_tournaments():
                try:
                    Tournament = []
                    with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                        reader  = csvfile.readlines() 
                        for row in reader:
                            Tournament.append(row)
                        return Tournament
                except ValueError: 
                    return f"Error message to be decided"
                
        Tournament = TournamentIO.get_tournaments()
        print(Tournament[userinput])



    if val == "8":
        Tournament_name = input("Name of tournament: ")
        Start_date = input("Start date of tournament 00/00/0000: ")
        End_date = input("End date of the tournament 00/00/0000: ")
        Venue = input("Select venue for the tournament: ")
        ContactPerson = input("Contact person: ")
        ContatEmail = input("Contact email: ")
        ContactPhone = input("Contact phone: ")

        tournament = [Tournament_name, Start_date, End_date, Venue, ContactPerson, ContatEmail, ContactPhone]

        class TournamentIO:
            def create_new_tournament(tournament_data: list):
                try: 
                    with open(TOURNAMENT_PATH, "a",newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(tournament) 
                    return f"New Tournament added :)"    
                except ValueError: 
                    f"Error message to be decided"

        print(TournamentIO.create_new_tournament(tournament))
    

    if val == "9":
        userinput = int(input("Select the game ID: "))
        class TournamentIO:
            def get_games():
                team_a = []
                team_b = []
                date = []
                try:
                    with open(GAMES_PATH, "r", encoding="utf-8") as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            team_a.append(row["team_a"])
                            team_b.append(row["team_b"])
                            date.append(row["match_date"])
                    return team_a, team_b, date
                except FileNotFoundError:
                    return "File not found"
                
        team_a, team_b, date = TournamentIO.get_games()
        print(team_a[userinput], "vs", team_b[userinput], "----->", date[userinput])


    if val == "10":
        tournament_name = input("Enter tournament name: ")
        round = input("Enter what round it is: ")
        match_number = input("match number: ")
        match_date = input("Enter match date: ")
        team_a = input("Enter team_a: ")
        team_b = input("Enter team_b: ")
        score_a = int(input("Enter score_a: "))
        score_b = int(input("Enter score_b: "))

            # Determine the winner
        if score_a > score_b:
            winner = team_a
        elif score_b > score_a:
            winner = team_b
        else:
            winner = "Draw" 
            
        games = [tournament_name, round, match_number, match_date, team_a, team_b, score_a, score_b, winner]

        class TournamentIO:
            def create_new_game(games: list):
                try:
                    with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(games)
                    return f"New Game added"
                except ValueError:
                    return "Error"
                
        print(TournamentIO.create_new_game(games))
        