from logic_layer.LL_api import LL_API
from Models.Player import Player
import os

class CaptainUI:
    def __init__(self):
        self.ll = LL_API()
        self.current_team_name: str | None = None

    # Chose which Captain or Team

    def _player_to_dict(self, p: Player) -> dict:
        '''Convert Player object to dict so we can comfortably use .get().'''
        return {
            "Name"        : p.name,
            "DOB"         : p.dob,
            "Address"     : p.address,
            "Phone number": p.phone,
            "Email"       : p.email,
            "Handle"      : p.handle,
            "Team"        : p.team,
            "Link"        : p.link,
        }

    def select_captain_and_team(self) -> bool:
        '''Make the user choose which team they are captain of.'''
        team_names, captains = self.ll.get_team_names_and_captains()

        if not team_names:
            print("There are no teams in the system yet.")
            return False

        print("\nAvailable teams / captains:")
        for i in range(len(team_names)):
            team_name = team_names[i]
            captain = captains[i]
            index = i + 1
            print(f"{index}) Team: {team_name} | Captain: {captain}")


        while True:
            choice = int(input("Enter team number to log in as captain: "))

            if 1 <= choice <= len(team_names):
                selected_team = team_names[choice - 1]
                self.current_team_name = selected_team
                print(f"\nYou are now captain of team: {self.current_team_name}")
                return True

            print(f"Please enter a number between 1 and {len(team_names)}.")
    

    def _get_and_show_team_members(self) -> list[Player]:
        '''Get team members for current team and print them.'''

        players = self.ll.get_team_members(self.current_team_name)

        if not players:
            print("There are currently no players in your team.")
            return []

        print(f"\nPlayers in {self.current_team_name}:")
        for index, p in enumerate(players, start=1):
            name = p.name
            print(f"{index}. {name}")
        return players

    def _get_and_show_available_players(self) -> list[Player]:
        '''Show all players that are NOT in any team.'''

        players: list[Player] = self.ll.get_available_players_for_captain(self.current_team_name)
        if not players:
            print("There are no free players to add.")
            return []

        # Sort alphabetically by Name
        players_sorted = sorted(players, key=lambda p: p.name.lower())

        print("\nAvailable players (no team yet):")
        for index, p in enumerate(players_sorted, start=1):
            print(f"{index}. {p.name}")
        return players_sorted


    def add_to_team(self):
        '''Captain adds a player that has no team to their team.'''

        players = self._get_and_show_available_players()
        if not players:
            return
        
        while True:
            selected = input("Enter the number of the player you want to add: \n")
            try:
                selected_index = int(selected) - 1
            except ValueError:
                print("Please enter a valid number")
                continue
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                continue
            break

        player_to_add = players[selected_index]
        player_name = player_to_add.name

        try:
            self.ll.add_player_to_team(self.current_team_name, player_name)
            print(f"\n{player_name} has been added to {self.current_team_name}.")
        except ValueError as error:
            print("Error:", error)

    def remove_from_team(self):
        '''Captain removes a player from their own team.'''

        all_players: list[Player] = self.ll.get_team_members(self.current_team_name)

        # Find the captain name for this team so we don't remove them
        team_names, captains = self.ll.get_team_names_and_captains()
        captain_name = None

        for i in range(len(team_names)):
            name = team_names[i]
            cap = captains[i]
            if name == self.current_team_name:
                captain_name = cap
                break

        # Exclude captain from removable list
        players: list[Player] = []
        for p in all_players:
            if p.handle != captain_name:
                players.append(p)

        if not players:
            print("There are no players to remove (only the captain exists).")
            return

        print(f"\nPlayers in {self.current_team_name} (excluding captain {captain_name}):\n")
       
        for index, p in enumerate(players, start=1):
            name = p.name
            handle = p.handle
            print(f"{index:2}. {name.ljust(15)} | Handle: {handle}")

        while True:
            selected = input("\nPlease enter the number of who you want to remove: ")
            try:
                selected_index = int(selected) - 1
            except ValueError:
                print("Please enter a valid integer")
                continue
            if selected_index < 0 or selected_index >= len(players):
                print("A player with this ID does not exist. Please enter a valid ID number.")
                continue
            break

        player_to_remove = players[selected_index]
        player_name = player_to_remove.name

        while True:
            confirmation = input(f"Are you sure you want to remove {player_name} from the team? Y/N ").strip().upper()

            if confirmation == "Y":
                    break
                    
            if confirmation == "N":
                print("Removal cancelled. The player will not be removed from the team.")
                return
            
            print("Please enter either Y/N")

        try:
            self.ll.remove_player_from_team(self.current_team_name, player_name)
            print("\033[92m┌────────────────────────────────────────────────────┐\033[0m")
            print(f"\033[92m {player_name} has been removed from the team.\033[0m")
            print("\033[92m└────────────────────────────────────────────────────┘\033[0m")
            user_inp = input("Press any button to return to start")
            if user_inp  != 1:
                if os.name == 'nt':
                    _ = os.system('cls')
                else:
                    _ = os.system('clear')
                
        except ValueError as error:
            print("Error:", error)

    def cap_see_player_info(self):
        '''Captain can see detailed info about a player in their own team.'''
        players = self._get_and_show_team_members()

        if not players:
            return
        while True:
            selected = input("Please enter the number of whose information you want to see: ").strip().lower()
            try:
                selected_index = int(selected) - 1
            except ValueError:
                print("please enter a valid integer")
                continue
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                continue
            break

        player_to_see = players[selected_index]
        player_name = player_to_see.name

        try:
            player: Player = self.ll.cap_view_player_info(player_name, self.current_team_name)
            info = self._player_to_dict(player)
            print(f"\n===Player Information for {player_name}===\n")
            for key, value in info.items():
                print(f"{key:12} : {value}")

            print("\nDo you want to edit this player's contact info?")
            choice = input("Change phone/address/email? (y/n): ").strip().lower()

            if choice != "y":
                return
        
            current_phone = info.get("Phonenumber", "")
            current_address = info.get("Address", "")
            current_email = info.get("Email", "")

            print("\nLeave field empty to keep current value.")
            new_phone = input(f"New phone  (current: {current_phone}): ").strip()
            new_address = input(f"New address (current: {current_address}): ").strip()
            new_email = input(f"New email   (current: {current_email}): ").strip()

            updated_player = self.ll.update_player_contact(
                player_name,
                self.current_team_name,
                new_phone,
                new_address,
                new_email
            )


            updated_dict = self._player_to_dict(updated_player)

            print("\nUpdated player info:")
            for key, value in updated_dict.items():
                print(f"{key}: {value}")



        except ValueError as error:
            print("Error:", error)

    def view_schedule(self,title="Current Games"):
        try:
            tournaments = self.ll.get_tournament_names() # Gets all tournament names
            print(tournaments)
            
            while True:
                tournament_name = input("Enter tournament name: ").strip()

                if tournament_name in tournaments: # Confirms that the tournament is in the system
                    break

                print("Tournament not found. Please enter a valid tournament name.")
            
            # Get all games/matches that are in the tournament 
            games = self.ll.get_game_by_tournament_name(tournament_name) 

            if not games: # If there are no games found
                print(f"No games found for tournament: {tournament_name}")
                return []
            
            print(f"\n=== {title} ===")
            for g in games: # Print information on every match/game
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
            
            return games
        
        except ValueError:
            print("Invalid input")