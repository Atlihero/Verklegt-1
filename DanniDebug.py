import csv


while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Create new player")
    print("3. get team")
    print("4. get player stats")
    print("5. Create new team")
    print("6. Get team stats")
    print("7. Get Tournament")
    print("8. Create Tournament")

    val = input("Veldu verkefni (1-6): ")


    #Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
    PLAYER_PATH: str = r"data_layer\_data\Players.csv"
    TEAM_PATH: str = r"data_layer\_data\Teams.csv"
    TOURNAMENT_PATH: str = r"data_layer\_data\Tournament.csv"

    
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
        wins = 0
        points = 0

        team = [teamName, captain, wins, points]
         
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
                Wins = []
                Points = []
                with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        Wins.append(row["Wins"])
                        Points.append(row["Points"])
                    return Wins, Points
        Wins, Points = TeamIO.get_team_stats() 
        print(f"{Wins[userinput]} Wins")
        print(f"{Points[userinput]} Points")

    
    if val == "7":
        userinput = int(input("Sláðu inn númer móts: "))
        class TouranmentIO:
            def get_tournaments():
                try:
                    Tournament = [] #Empty list in which the tournament that is chosen goes into
                    with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                        reader  = csvfile.readlines() #reads the lines in the csv
                        for row in reader: #for loop that goes through the lines to look for the right tournament
                            Tournament.append(row) #append the tournament chosen to the list
                        return Tournament #returns the list
                except ValueError: #in case of wrong inputs
                    return f"Error message to be decided"
                
        Tournament = TouranmentIO.get_tournaments()
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
