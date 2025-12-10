from logic_layer.LL_api import LL_API
from Models.Tournament import Tournament
api = LL_API()

def show_games(games, title="Current Games"):
    print(f"\n=== {title} ===")
    for g in games:
        print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
              f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Get team")
    print("3. Create tournament")
    print("4. create tournament with games")
    print("5. Update results")
    print("6. Show Games")
    print("q. Quit")

    val = input("Veldu verkefni (1-6): ")

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
                return api.create_new_tournament(tournament_dict)

        organizer = Organizer()
        tournament = organizer.createTournament()
        print("Tournament has been created:", tournament)

    if val == "4":
        class OrganizerUI():

            def createTournament(self):
                lapi = LL_API()
            
                while True:
                    unique_name = input("Create a unique name for the tournament: ")
                    try:
                        unique_name = lapi.valid_tournament_name(unique_name)
                        break
                    except ValueError as error:
                        print(error)

                while True:
                    start_date = input("Select the start date of the tournament: ")
                    try:
                        start_date = lapi.valid_start_date(start_date)
                        break
                    except ValueError as error:
                        print(error)

                while True:
                    end_date = input("Select the end date of the tournament: ")
                    try:
                        end_date = lapi.valid_end_date(end_date, start_date)
                        break
                    except ValueError as error:
                        print(error)

                venue = input("Enter the name of a venue (location) for the tournament: ")
                
                contact_person = input("Name the contact person for this tournament: ")
                
                while True:
                    contact_email = input("What is the contact email for this tournament: ")
                    try: 
                        lapi.valid_email(contact_email)
                        break
                    except ValueError as error:
                        print(error)
                
                while True:
                    contact_phone = input("What is the contact phone for this tournament: ")
                    try:
                        lapi.valid_phone(contact_phone)
                        break
                    except ValueError as error:
                        print(error)
                
            # have it as an object not an dict so it is easier to return and read.
                tournament_obj = Tournament( 
                    unique_name=unique_name,
                    start_date=start_date,
                    end_date=end_date,
                    venue=venue,
                    contact_person=contact_person,
                    contact_email=contact_email,
                    contact_phone=contact_phone
                )
                lapi.generateGames(unique_name, start_date)
                return lapi.create_new_tournament(tournament_obj)
        
        ui = OrganizerUI()
        created_tournament = ui.createTournament()
        print(created_tournament)
                
        

    if val == "5":
        class Organizer:
            tournament_name = input("Enter tournament name: ").strip()
            games = api.get_game_by_tournamentName(tournament_name)

            if not games:
                print("\nNo games found for this tournament.\n")

            show_games(games, "Current Games")

            match_number = int(input("\nEnter match number to update: "))
            score_a = int(input("Enter score for team A: "))
            score_b = int(input("Enter score for team B: "))

            result = api.updateGame(tournament_name, match_number, score_a, score_b)

            winner = result["winner"]
            tournament_name = result["tournament_name"]

            if winner:
                advance_result = api.advance_round(tournament_name, match_number, winner)
                print(advance_result)

                if result["round"] == "F":
                    print("\n==============================")
                    print(f"🏆  TOURNAMENT WINNER: {winner}  🏆")
                    print("==============================\n")

            else:
                print("Game is a draw. Winner cannot advance.")

            updated_games = api.get_game()
            show_games(updated_games, "Updated Games")

        
    if val == "6":
        class PublicViewer:
            def view_schedule(games, title="Current Games"):
                print(f"\n=== {title} ===")
                for g in games:
                    print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                        f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
                return games

        tournament_name = input("Enter tournament name: ").strip()
        games = api.get_game_by_tournamentName(tournament_name)

        schedule = PublicViewer.view_schedule(games)

    if val == "q":
        print("You have quit the program")
        break