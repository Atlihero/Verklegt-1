from logic_layer.LL_api import LL_API
from Models.Tournament import Tournament
from Models.Player import Player
from ui_layer.Happy_path import Happy_paths


def show_games(games, title="Current Games") -> str:
    '''Gets the schedule for the games.'''
    
    print(f"\n=== {title} ===\n")
    print(f"{'No':<3}  {'Round':<8} {'Date':<12} {'Match':<49} {'Score':<7} {'Winner'}")
    print("-" * 105)

    for g in games: # Print information on every match/game
    
        match = f"{g['team_a']} vs {g['team_b']}"
        score = f"{g['score_a'] or '-'}-{g['score_b'] or '-'}"
        print(f"{g['match_number']:<4}| {g['round']:<5} | {g['match_date']:<11} | {match:<47} | {score:<5} | {g['winner'] or '-'}")
    print()
    return games


class OrganizerUI():

    def __init__(self):
        self.lapi = LL_API()


    def create_player(self) -> Player:
        '''Have the user input all the information needed for the player.'''

        running = True
        print("\n=== Create a New Player ===")
        while True: # Check if name of player is a valid input
            name = input("Enter full name of player: ")
            if name == "q":
                running = False
                break
            try:
                name = self.lapi.valid_name(name)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if player's date of birth is a valid input
            dob_str = input("Enter player date of birth (DD/MM/YYYY): ")
            if dob_str == "q":
                running = False
                break
            try:
                dob = self.lapi.valid_dob(dob_str)
                break
            except ValueError as error:
                print(f"Error: {error}")
            
        while running: # Check if player's home address is a valid input
            address = input("Enter player's home address: ")
            if address == "q":
                running = False
                break
            try:
                address = self.lapi.valid_address(address)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
    
        while running: # Check if player's phone number is a valid input
            phone_number = "354" + input("Enter player's phone number (354): ")
            if phone_number == "q":
                running = False
                break
            try:
                phone_number = self.lapi.valid_phone(phone_number)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if player's email address is a valid input
            player_email = input("Enter the player's email address: ")
            if player_email == "q":
                running = False
                break
            try: 
                self.lapi.valid_email(player_email)
                break
            except ValueError as error:
                print(f"Error: {error}")
    
        while running: # Check if player's handle is a valid input
            handle = input("Enter player's handle: ")
            if handle == "q":
                running = False
                break
            try:  
                handle = self.lapi.valid_handle(handle)
                break
            except ValueError as error:
                print(error)

        while running: # Check if player's link is a valid input
            link = input("Enter a link (press 'Enter' to skip): ")
            if running == "q":
                running = False
                break
            try:
                link = self.lapi.validate_link(link)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running:
            # Create the player object using valid fieldnames
            player_obj = Player(
                name = name,
                dob = dob_str,
                address = address,
                phone = phone_number,
                email = player_email,
                handle = handle,
                team = None, # Player start with no team
                link = link
            )

            return self.lapi.create_player(player_obj) and Happy_paths.player_was_made()


    def createTournament(self) -> Tournament:
        '''Input every information needed to create a tournament.'''
        
        print("\n=== Create a New Tournament ===")
        running = True
        while running: # Check if tournamnent name is a valid input
            unique_name = input("Create a unique name for the tournament: ").strip()
            if unique_name == "q":
                running = False
                break
            try:
                unique_name = self.lapi.valid_tournament_name(unique_name)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if tournament start date is a valid input
            start_date = input("Select the start date of the tournament. DD/MM/YYYY: ")
            if start_date == "q":
                running = False
                break
            try:
                start_date = self.lapi.valid_start_date(start_date)
                break
            except ValueError as error:
                print(f"Error: {error}. Start date has to be in the future.")

        while running: # Check if tournament end date is a valid input
            end_date = input("Select the end date of the tournament. DD/MM/YYYY: ")
            if end_date == "q":
                running = False
                break
            try:
                end_date = self.lapi.valid_end_date(end_date, start_date ,min_days=5)
                break
            except ValueError as error:
                print(f"Error: {error}. End date must be at least 5 days after the start date.")

        while running: # Check if tournament location is a valid input
            venue = input("Enter the name of a venue (location) for the tournament: ")
            if venue == "q":
                running = False
                break
            try:
                venue = self.lapi.valid_tournament_location(venue)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
        while running: # Check if tournament contact name is a valid input
            contact_person = input("Who is the contact person for this tournament. Please enter a name: ")
            if contact_person == "q":
                running = False
                break
            try:
                contact_person = self.lapi.valid_tournament_contact(contact_person)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
        while running: # Check if tournamnent contact email is a valid input
            contact_email = input("What is the contact person's email. Please enter an email address: ")
            if contact_email == "q":
                running = False
                break
            try: 
                self.lapi.valid_email(contact_email)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
        while running: # Check if tournamnent contact phone number is a valid input
            contact_phone = "354" + input("What is the contact person's phone number. Please enter a phone number (354): ")
            if contact_phone == "q":
                running = False
                break
            try:
                self.lapi.valid_phone(contact_phone)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
        while running:
            # Create the tournament object with valid fieldnames
            tournament_obj = Tournament( 
                unique_name = unique_name,
                start_date = start_date,
                end_date = end_date,
                venue = venue,
                contact_person = contact_person,
                contact_email = contact_email,
                contact_phone = contact_phone
            )
            self.lapi.generate_games(unique_name, start_date)
            return self.lapi.create_new_tournament(tournament_obj)
            

    def update_result(self) -> str:
        '''Update results of the tournament.'''
        try:
            tournaments = self.lapi.get_tournament_names() # List of all tournament names
            print()
            print(f"Tournaments in the system: {tournaments}")

            running = True
            
            while running: # Select a tournament that is already made
                tournament_name = input("\nPlease enter a tournament name: ").strip()
                if tournament_name == "q":
                    running = False
                    break
                if tournament_name in tournaments:
                    break
                print("Tournament was not found. Please enter a valid tournament name.")
            
            if running:
                # Get all games from the inputted tournament
                games = self.lapi.get_game_by_tournament_name(tournament_name)

                if not games:
                    print("\nNo games were found for this tournament.\n")

                show_games(games, "Current Games")

            while running:
                try:
                    '''Enter the match number to edit and the scores of both teams with error handling
                    on negative and invalid inputs'''

                    match_number = int(input("Enter match number to update: "))
                    score_a = int(input("Enter score for team A: "))
                    score_b = int(input("Enter score for team B: "))

                    if match_number == "q":
                        running = False
                        break

                    if score_a == "q":
                        running = False
                        break

                    if score_b == "q":
                        running = False
                        break

                    if match_number < 0 or score_a < 0 or score_b < 0:
                        print("Numbers cannot be negative. Please enter non-negative integers.")
                        continue
                    break
                except ValueError:
                    print("Scores and match number must be integer numbers. Please enter valid numbers.")
            
            # Updates the game/match results
            if running:
                result = self.lapi.update_game(tournament_name, match_number, score_a, score_b)

                # If a draw occurs the scores must be inputted again until there is a clear winner
                while result["winner"] is None:
                    print(f"The game between {result['team_a']} and {result['team_b']} ended in a draw. Please enter new scores.")
                    score_a = int(input(f"Score for {result['team_a']}: "))
                    score_b = int(input(f"Score for {result['team_b']}: "))
                    result = self.lapi.update_game(tournament_name, match_number, score_a, score_b)

                winner = result["winner"]
                tournament_name = result["tournament_name"]

                # The winner of the match advances to the next round
                advance_result = self.lapi.advance_round(tournament_name, match_number, winner)
                print(advance_result)

                # If it is the Finals (F) the team that wins that game is the tournament winner'''
                if result["round"] == "F":
                    print("\n==============================")
                    print(f" TOURNAMENT WINNER: {winner} ")

                updated_games = self.lapi.get_game_by_tournament_name(tournament_name)
                show_games(updated_games, "Updated Games") # Shows updated match/game list
            
        except ValueError as error:
            print(f"Invalid input: {error}")


    def create_team_ui(self) -> str:
        '''Creates a new team and captain using create player things from earlier'''

        print("\n=== Create a New Team ===")
        running = True

        while True:
            team_name = input("Enter the team Name (or 'q' to quit): ").strip()
            if team_name.lower() == "q":
                print("Team creation cancelled.")
                return None
            try:
                team_name = self.lapi.valid_team_name(team_name)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if name of player is a valid input
            print("\n=== Create a Captain ===")
            name = input("Enter full name of player: ")
            if name == "q":
                running = False
                break
            try:
                name = self.lapi.valid_name(name)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if player's date of birth is a valid input
            dob_str = input("Enter player date of birth (DD/MM/YYYY): ")
            if dob_str == "q":
                running = False
                break
            try:
                dob = self.lapi.valid_dob(dob_str)
                break
            except ValueError as error:
                print(f"Error: {error}")
            
        while running: # Check if player's home address is a valid input
            address = input("Enter player's home address: ")
            if address == "q":
                running = False
                break
            try:
                address = self.lapi.valid_address(address)
                break
            except ValueError as error:
                print(f"Error: {error}")
        
        while running: # Check if player's phone number is a valid input
            phone_number = "354" + input("Enter player's phone number (354): ")
            if phone_number == "q":
                running = False
                break
            try:
                phone_number = self.lapi.valid_phone(phone_number)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running: # Check if player's email address is a valid input
            player_email = input("Enter the player's email address: ")
            if player_email == "q":
                running = False
                break
            try: 
                self.lapi.valid_email(player_email)
                break
            except ValueError as error:
                print(f"Error: {error}")
    
        while running: # Check if player's handle is a valid input
            handle = input("Enter player's handle: ")
            if handle == "q":
                running = False
                break
            try:  
                handle = self.lapi.valid_handle(handle)
                break
            except ValueError as error:
                print(error)

        while running: # Check if player's link is a valid input
            link = input("Enter a link (press 'Enter' to skip): ")
            if link == "q":
                running = False
                break
            try:
                link = self.lapi.validate_link(link)
                break
            except ValueError as error:
                print(f"Error: {error}")

        while running:
            # Create the player object using valid fieldnames
            player_obj = Player(
                name = name,
                dob = dob_str,
                address = address,
                phone = phone_number,
                email = player_email,
                handle = handle,
                team = team_name,
                link = link
            )
            empty = self.lapi.create_player(player_obj)
            ascii_logo = input("Enter ASCII Logo (optional): ").strip() or None

            new_team = self.lapi.add_team(name=team_name, captain=handle, asciiLogo=ascii_logo)
            print(f"Team '{new_team.name}' has been successfully created!")
            return new_team and Happy_paths.team_was_made()
        

    def organizer_see_info(self) -> None:
        '''The organizer can see player information for every player in the tournament'''

        running = True
        player = self.lapi.organizer_view_player_info() # Get list of players and their team
        print(f"\n=== Player Information ===")
        while running:
            try:
                userinput = input(f"\nSelect a player ID between 1-{len(player)}: ")
                if userinput == "q":
                    running = False
                    break

                real_userinput = int(userinput) - 1
                if 0 <= int(real_userinput) <= len(player): # Check if the input is valid
                        break
                else:
                    print("A player with this ID does not exist. Please enter a valid ID number.")
            except ValueError:
                    print("The input has to be an integer number. Please enter a valid number.") 
        
        if running:
            print(f"{player[real_userinput]}\n") # Show the player
        
    
    def view_schedule(self, title="Current Games") -> str:
        '''Return the schedule for the games so it can be viewed.'''
        try:
            tournaments = self.lapi.get_tournament_names() # Gets all tournament names
            print()
            print(f"Torunaments in the system: {tournaments}")
            
            while True:
                tournament_name = input("\nPlease enter a tournament name: ").strip()

                if tournament_name in tournaments: # Confirms that the tournament is in the system
                    break

                print("Tournament not found. Please enter a valid tournament name.")
            
            # Get all games/matches that are in the tournament 
            games = self.lapi.get_game_by_tournament_name(tournament_name) 

            if not games: # If there are no games found
                print(f"No games found for tournament: {tournament_name}")
                return []
            
            print(f"\n=== {title} ===\n")
            print(f"{'No':<3}  {'Round':<8} {'Date':<12} {'Match':<49} {'Score':<7} {'Winner'}")
            print("-" * 105)

            for g in games: # Print information on every match/game
                match = f"{g['team_a']} vs {g['team_b']}"
                score = f"{g['score_a'] or '-'}-{g['score_b'] or '-'}"
                print(f"{g['match_number']:<4}| {g['round']:<5} | {g['match_date']:<11} | {match:<47} | {score:<6} | {g['winner'] or '-'}")
            
            print()
            return games
        
        except ValueError:
            print("Invalid input")

