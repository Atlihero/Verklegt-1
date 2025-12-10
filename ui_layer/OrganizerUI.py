from logic_layer.LL_api import LL_API
from Models.Tournament import Tournament
from Models.Player import Player


def show_games(games, title="Current Games"):
    print(f"\n=== {title} ===")
    for g in games:
        print(f"{g['match_number']:>2}: {g['round']} {g['match_date']}| {g['team_a']} vs {g['team_b']} | "
              f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")


class OrganizerUI():

    def __init__(self):
        self.lapi = LL_API()


    def create_player(self):
    
        while True:
            name = input("Enter full name of player: ")
            try:
                name = self.lapi.valid_name(name)
                break
            except ValueError as error:
                print(error)


        while True:
            dob_str = input("Enter player date of birth (DD/MM/YYYY): ")
            try:
                dob = self.lapi.valid_dob(dob_str) #blud are we fr dob er síðan ekkert notað
                break
            except ValueError as error:
                print(error)
            
        while True:
            address = input("Enter player's home address: ")
            try:
                address = self.lapi.valid_address(address)
                break
            except ValueError as error:
                print(error) 
        
    
        while True:
            phone_number = input("Enter player's phone number: ")
            try:
                self.lapi.valid_phone(phone_number)
                break
            except ValueError as error:
                print(error)

        while True:
            player_email = input("Enter the player's email address: ")
            try: 
                self.lapi.valid_email(player_email)
                break
            except ValueError as error:
                print(error)
    
        while True:
            handle = input("Enter player's handle: ")
            try:  
                handle = self.lapi.valid_handle(handle)
                break
            except ValueError as error:
                print(error)

        while True:
            link = input("Enter a link (press 'Enter' to skip): ")
            try:
                link = self.lapi.validate_link(link)
                break
            except ValueError as error:
                print(error)


        player_obj = Player(
            name = name,
            dob = dob_str,
            address = address,
            phone = phone_number,
            email = player_email,
            handle = handle,
            link = link,
            team = None,
        )

        return self.lapi.create_player(player_obj)

        #player = self.lapi.create_new_player(name, dob, address, phone_number, player_email, handle, link)
        #print("Player created successfully!")
        #return player

    def createTournament(self):
    
        while True:
            unique_name = input("Create a unique name for the tournament: ")
            try:
                unique_name = self.lapi.valid_tournament_name(unique_name)
                break
            except ValueError as error:
                print(error)

        while True:
            start_date = input("Select the start date of the tournament: ")
            try:
                start_date = self.lapi.valid_start_date(start_date)
                break
            except ValueError as error:
                print(error)

        while True:
            end_date = input("Select the end date of the tournament: ")
            try:
                end_date = self.lapi.valid_end_date(end_date, start_date)
                break
            except ValueError as error:
                print(error)

        while True:
            venue = input("Enter the name of a venue (location) for the tournament: ")
            try:
                venue = self.lapi.valid_tournament_location(venue)
                break
            except ValueError as error:
                print(error)
        
        while True:
            try:
                contact_person = input("Name the contact person for this tournament: ")
                contact_person = self.lapi.valid_tournament_contact(contact_person)
                break
            except ValueError as error:
                print(error)
        
        while True:
            contact_email = input("What is the contact email for this tournament: ")
            try: 
                self.lapi.valid_email(contact_email)
                break
            except ValueError as error:
                print(error)
        
        while True:
            contact_phone = input("What is the contact phone for this tournament: ")
            try:
                self.lapi.valid_phone(contact_phone)
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

        return self.lapi.create_new_tournament(tournament_obj)

    def update_result(self):
        tournaments = self.lapi.get_tournament_names()
        print(tournaments)
        tournament_name = input("Enter tournament name: ").strip()
        games = self.lapi.get_game_by_tournamentName(tournament_name)

        if not games:
            print("\nNo games found for this tournament.\n")

        show_games(games, "Current Games")

        match_number = int(input("\nEnter match number to update: "))
        score_a = int(input("Enter score for team A: "))
        score_b = int(input("Enter score for team B: "))

        result = self.lapi.updateGame(tournament_name, match_number, score_a, score_b)

        winner = result["winner"]
        tournament_name = result["tournament_name"]

        # If a winner exists, advance
        if winner:
            advance_result = self.lapi.advance_round(tournament_name, match_number, winner)
            print(advance_result)

            if result["round"] == "F":
                print("\n==============================")
                print(f" TOURNAMENT WINNER: {winner} ")

        else:
            print("Game is a draw. Winner cannot advance.")


        updated_games = self.lapi.get_game()
        show_games(updated_games, "Updated Games")


    def create_team_ui(self):
        print("\n=== Create a New Team ===")
                
        team_name = input("Enter Team Name: ").strip()
        captain = None
        ascii_logo = input("Enter ASCII Logo (optional): ").strip() or None

        new_team = self.lapi.add_team(name=team_name, captain=captain, asciiLogo=ascii_logo)
        print(f"Team '{new_team.name}' created successfully!")
        return new_team

    def organizer_see_info(self) -> None:
        '''The organizer can see player information for every player in the tournament'''
        userinput = int(input("Veldu ID leikmanns milli 1-48: ")) 
        player = self.lapi.organizer_view_player_info()
        print(f"Player: {player[userinput]}")

#vantar create captain!!!
