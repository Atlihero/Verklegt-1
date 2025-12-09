from logic_layer.LL_api import LL_API
from Models.Tournament import Tournament
lapi = LL_API()

def show_games(games, title="Current Games"):
    print(f"\n=== {title} ===")
    for g in games:
        print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
              f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")

class OrganizerUI():
        def createTournament(self):
            
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
        
        def update_result(self):
            tournament_name = input("Enter tournament name: ").strip()
            games = lapi.get_game_by_tournamentName(tournament_name)

            if not games:
                print("\nNo games found for this tournament.\n")

            show_games(games, "Current Games")

            match_number = int(input("\nEnter match number to update: "))
            score_a = int(input("Enter score for team A: "))
            score_b = int(input("Enter score for team B: "))

            result = lapi.updateGame(match_number, score_a, score_b)

            winner = result["winner"]
            tournament_name = result["tournament_name"]

            # If a winner exists, advance
            if winner:
                advance_result = lapi.advance_round(tournament_name, match_number, winner)
                print(advance_result)

                # ⭐ IF THIS WAS THE FINAL MATCH (F = match 15), SHOW WINNER BANNER
                if result["round"] == "F":
                    print("\n==============================")
                    print(f"🏆  TOURNAMENT WINNER: {winner}  🏆")
                    print("==============================\n")

            else:
                print("Game is a draw. Winner cannot advance.")

            updated_games = lapi.get_game()
            show_games(updated_games, "Updated Games")


        def organizer_see_info(self) -> None:
            '''The organizer can see player information for every player in the tournament'''
            try:
                players = self.ll.organizer_view_player_info()
            except ValueError as error:
                print("Error: ", error)
                return
            
            if not players:
                print("There are no players in the tournament.")
                return

            for p in players:
                print(f"\nPlayer Information for {p.get('Name')}:")
                for attr, value in vars(p).items():
                    print(f"{attr}: {value}")
