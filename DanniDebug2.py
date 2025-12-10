from logic_layer.LL_api import LL_API

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Get team")
    print("3. create tournament with games")
    print("4. Update results")
    print("q. Quit")

    val = input("Veldu verkefni (1-4): ")

    if val == "1":
        userinput = int(input("Veldu ID leikmanns milli 1-57: "))
        class PublicViewer:     
            def getplayerPublic():
                api = LL_API()        
                players = api.get_playerPublic()
                return players
                
            player, team = getplayerPublic()
            print(f"Player: {player[userinput]}, Team: {team[userinput]}")

    if val == "2":
        userinputTeams = int(input("Veldu númer liðs 1-18: "))
        class PublicViewer:

            def getTeamPublic():
                api = LL_API()
                teams = api.get_teams_public()
                return teams

            teams, captain = getTeamPublic()
            print(f"Team: {teams[userinputTeams]}, Captain: {captain[userinputTeams]}")

    
    if val == "3":
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
                ll.create_new_tournament(tournament_dict)

                print("\nGenerating random games for this tournament...\n")
                ll.generateGames(name, start)

                print("\nTournament created and games generated successfully.\n")
        
        Organizer.UI_create_tournament()


    if val == "4":
        class Organizer:
            ll = LL_API()
            games = ll.get_game()

            print("\n=== Current Games ===")
            for g in games:
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")

            # Get user input
            match_number = int(input("\nEnter match number to update: "))
            score_a = int(input("Enter score for team A: "))
            score_b = int(input("Enter score for team B: "))

            result = ll.updateGame(match_number, score_a, score_b)
            winner = result["winner"]
            tournament_name = result["tournament_name"]

            if winner:
                advance_result = ll.advance_round(tournament_name, match_number, winner)
                print(advance_result)
            else:
                print("Game is a draw. Winner cannot advance.")

            updated_games = ll.get_game()
            print("\n=== Updated Games ===")
            for g in updated_games:
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")

    if val == "q":
        print("You have quit the program")
        break