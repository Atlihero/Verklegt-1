from logic_layer.LL_api import LL_API
from data_layer.data_api import DataAPI
from Models.Player import Player

import os

class CaptainUI:
    def __init__(self):
        self.ll = LL_API()
        self.data_api = DataAPI()
        self.current_team_name: str | None = None


    def _player_to_dict(self, player: Player) -> dict:
        '''Convert Player object to dictionary'''
        
        return {
            "Name"        : player.name,
            "DOB"         : player.dob,
            "Address"     : player.address,
            "Phone number": player.phone,
            "Email"       : player.email,
            "Handle"      : player.handle,
            "Team"        : player.team,
            "Link"        : player.link,
        }


    def select_captain_and_team(self) -> bool:
        '''Make the user choose which team they are captain of.'''
        team_names, captains = self.ll.get_team_names_and_captains()

        if not team_names:
            print("There are no teams in the system yet.")
            return False

        print("\n===Available teams/captains===\n")
        for i in range(len(team_names)):
            team_name = team_names[i]
            captain = captains[i]
            index = i + 1
            print(f"{index:3}) Team: {team_name:25} | Captain: {captain:12}")
        print()

        while True:
            try:
                choice = input("Enter team number to log in as captain or q to quit: ").strip().lower()
                if choice == "q":
                    return False

                elif 1 <= int(choice) <= len(team_names):
                    selected_team = team_names[int(choice) - 1]
                    self.current_team_name = selected_team
                    print(f"\nYou are now captain of team: {self.current_team_name}")
                    return True
            except ValueError:
                print(f"Please enter a number between 1 and {len(team_names)}.")
    

    def _get_and_show_team_members(self) -> list[Player]:
        '''Get team members for current team and print them.'''

        players = self.ll.get_team_members(self.current_team_name)

        if not players:
            print("There are currently no players in your team.")
            return []

        print(f"\n==Players in {self.current_team_name}==\n")
        for index, player in enumerate(players, start=1):
            name = player.name
            print(f"{index}. {name}")
        return players


    def _get_and_show_available_players(self) -> list[Player]:
        '''Show all players that are not in any team.'''

        players: list[Player] = self.ll.get_available_players_for_captain(self.current_team_name)
        if not players:
            print("There are no free players to add.\n")
            return []

        # Sort alphabetically by Name
        players_sorted = sorted(players, key=lambda p: p.name.lower())

        print("\n==Available players (no team yet)==\n")
        for index, p in enumerate(players_sorted, start=1):
            print(f"{index:2}. {p.name.ljust(15)}")

        return players_sorted


    def add_to_team(self) -> str:
        '''Captain adds a player that has no team to their team.'''

        players = self._get_and_show_available_players()
        if not players:
            return
        
        while True:
            selected = input("\nEnter the number of the player you want to add: ").strip().lower()
            if selected == "q":
                return
            try:
                selected_index = int(selected) - 1
            except ValueError:
                print("Please enter a valid number.")
                continue
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                continue
            break

        player_to_add = players[selected_index]
        player_name = player_to_add.name

        try:
            self.ll.add_player_to_team(self.current_team_name, player_name)
            print("\033[92m┌────────────────────────────────────────────────────┐\033[0m")
            print(f"\033[92m {player_name} has been added to {self.current_team_name}.\033[0m")
            print("\033[92m└────────────────────────────────────────────────────┘\033[0m")
        except ValueError as error:
            print("Error:", error)


    def remove_from_team(self) -> str:
        '''Captain removes a player from their own team.'''

        all_players: list[Player] = self.ll.get_team_members(self.current_team_name)

        # Find the captain for the team
        team_names, captains = self.ll.get_team_names_and_captains()
        captain_name = None

        for i in range(len(team_names)):
            name = team_names[i]
            cap = captains[i]
            if name == self.current_team_name:
                captain_name = cap
                break

        # Exclude captain from removable list, because he is the player removing others
        players: list[Player] = []
        for p in all_players:
            if p.handle != captain_name:
                players.append(p)

        if not players:
            print("There are no players to remove (only the captain exists). Please add players in your team to be able to remove them.\n")
            return

        print(f"\n==Players in {self.current_team_name} (excluding captain {captain_name})==\n")
       
        for index, p in enumerate(players, start=1):
            name = p.name
            handle = p.handle
            print(f"{index:2}. {name.ljust(15)} | Handle: {handle}")

        while True:
            selected = input("\nPlease enter the number of who you want to remove: ").strip().lower()
            if selected == "q":
                return
            try:
                selected_index = int(selected) - 1
            except ValueError:
                print("The input has to be a valid integer. Please try again.")    
            
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
                print("Removal cancelled. The player will not be removed from the team.\n")
                return
            
            print("Please enter either Y/N")

        try:
            self.ll.remove_player_from_team(self.current_team_name, player_name)
            print("\033[92m┌────────────────────────────────────────────────┐\033[0m")
            print(f"\033[92m {player_name} has been removed from the team.\033[0m")
            print("\033[92m└────────────────────────────────────────────────┘\033[0m")
            user_inp = input("Press any button to return to start")
            if user_inp  != 1:
                if os.name == 'nt':
                    _ = os.system('cls')
                else:
                    _ = os.system('clear')
                
        except ValueError as error:
            print("Error:", error)


    def cap_see_player_info(self) -> str:
        '''Captain can see personal information about the player's in his own team.'''
        players = self._get_and_show_team_members()

        if not players:
            return
        
        selected = input("\nPlease enter the number of whose information you want to see: ").strip().lower()
        if selected == "q":
            return
        selected_index = int(selected) - 1
        if selected_index < 0 or selected_index >= len(players):
            print("The number is not in the player's number range. Please select another number.")
            return
        
        while True:
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
        player_handle = player_to_see.handle

        try:
            player: Player = self.ll.cap_view_player_info(player_handle, self.current_team_name)
            info = self._player_to_dict(player)
            print(f"\n===Player Information for {player_handle}===\n")
            for key, value in info.items():
                print(f"{key:12} : {value}")

            print("\nDo you want to edit this player's contact info?")
            choice = input("Change phone/address/email? (Y/N): ").strip().lower()

            if choice != "y":
                return
    
            print("\nLeave field empty to keep current value.")
            while True:
                try:
                    new_phone_input = input("Enter the player's new phone number (354). Press enter to keep old phone number: ")
                    if new_phone_input == "":
                        new_phone = self.ll.keep_old_phone("", player.phone)
                    else:
                        new_input = "354" + new_phone_input 
                        new_phone = self.ll.keep_old_phone(new_input, player.phone)
                    break
                except ValueError as error:
                    print(f"Error: {error}")
            
            while True:
                try:
                    new_address_input = input("Enter player's new home address. Press enter to keep the old one: ").strip()
                    new_address = self.ll.keep_old_address(new_address_input, player.address)
                    break
                except ValueError as error:
                    print(f"Error: {error}")
               
            while True:
                try: 
                    new_email_input = input("Enter the player's email addres. Press enter to keep old email address: ")
                    new_email = self.ll.keep_old_email(new_email_input, player.email)
                    break
                except ValueError as error:
                    print(f"Error: {error}")

            updated_player = self.ll.update_player_contact(player_handle, self.current_team_name, new_phone, new_address, new_email)
            
        except ValueError as error:
            print("Error:", error)
        
        updated_dict = self._player_to_dict(updated_player)
        print("\n===Updated player info===\n")
        for key, value in updated_dict.items():
                print(f"{key:13}: {value}")
        print()


    def view_schedule(self,title="Current Games") -> str:
        try:
            tournaments = self.ll.get_tournament_names() # Gets all tournament names
            print()
            print(f"Tournaments in the system: {tournaments}")
            
            while True:
                tournament_name = input("Enter tournament name: ").strip().lower()
                if tournament_name == "q":
                    break

                elif tournament_name in tournaments: # Confirms that the tournament is in the system
                    break

                print("Tournament not found. Please enter a valid tournament name.")
            
            # Get all games/matches that are in the tournament 
            games = self.ll.get_game_by_tournament_name(tournament_name) 

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