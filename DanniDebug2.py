from logic_layer.LL_api import LL_API

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Get team")
    print("3. Create tournament")
    print("4. create tournament with games")
    print("5. Update results")
    print("q. Quit")

    val = input("Veldu verkefni (1-5): ")

    if val == "1":
        userinput = int(input("Veldu ID leikmanns milli 1-57: "))
        class PublicViewer:     
            def getplayerPublic():
                api = LL_API()        
                players = api.getPlayerpublic()
                return players
                
            player, team = getplayerPublic()
            print(f"Player: {player[userinput]}, Team: {team[userinput]}")

    if val == "2":
        userinputTeams = int(input("Veldu númer liðs 1-18: "))
        class PublicViewer:

            def getTeamPublic():
                api = LL_API()
                teams = api.getTeamPublic()
                return teams

            teams, captain = getTeamPublic()
            print(f"Team: {teams[userinputTeams]}, Captain: {captain[userinputTeams]}")

    
    if val == "3":
        class Organizer:
            def createTournament(self):
                unique_name = input("Create a unique name for the tournament: ")
                start_date = input("Select the start date of the tournament: ")
                end_date = input("Select end date for the tournament: ")
                venue = input("Select the venue for the tournament: ")
                contact_person = input("Name the contact person for this tournament: ")
                contact_email = input("What is the contact email for this tournament: ")
                contact_phone = input("What is the contact phone for this tournament: ")
                tournament_dict = {
                    "unique_name": unique_name,
                    "start_date": start_date,
                    "end_date": end_date,
                    "venue": venue,
                    "contact_person": contact_person,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone
                }
                api = LL_API()
                return api.create_new_tournaments(tournament_dict)

        organizer = Organizer()
        tournament = organizer.createTournament()
        print("Tournament has been created:", tournament)

    if val == "4":
        class Organizer:
            def UI_create_tournament():
                print("\n=== Create New Tournament ===")
                name = input("Enter tournament name: ")
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                venue = input("Venue: ")
                contact = input("Contact person: ")
                email = input("Contact email: ")
                phone = input("Contact phone: ")

                tournament_dict = {
                    "unique_name": name,
                    "start_date": start,
                    "end_date": end,
                    "venue": venue,
                    "contact_person": contact,
                    "contact_email": email,
                    "contact_phone": phone
                }
                ll = LL_API()
                ll.create_new_tournaments(tournament_dict)

                print("\nGenerating random games for this tournament...\n")
                ll.generateGames(name)

                print("\nTournament created and games generated successfully.\n")
        
        Organizer.UI_create_tournament()


    if val == "5":
        class Organizer:
            ll = LL_API()
            games = ll.get_game()  # assuming you have a method to get all games
            print("\n=== Current Games ===")
            for g in games:
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")

            match_number = int(input("\nEnter match number to update: "))
            score_a = int(input("Enter score for team A: "))
            score_b = int(input("Enter score for team B: "))

            result = ll.updateGame(match_number, score_a, score_b)
            print(result)
    
    if val == "q":
        print("You have quit the program")
        break