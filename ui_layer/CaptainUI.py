from logic_layer.LL_api import LL_API

class CaptainUI:
    def __init__(self):
        self.ll_api = LL_API()


    def _team_is_selected(self) -> bool:

        if self.current_team_name == None:
            return True
        return self.select_team_captain()
    
    '''def _select_players(self, players: list[dict], title = "Players in your team: ") -> dict:
        Function that displays and returns the selected player dict.
        print(f"\n{title}")
        for index, p in enumerate(players, start=1):
            print(f"{index}. {p.get('Name')} | Handle: {p.get('Handle')}")

        try:
            selected = input("Please enter the number of who you want to remove or b to go back: ").strip()
            selected_index = int(selected) - 1

            if selected == "b":
                return None
            
            if not selected.isdigit():
                print("Invalid input. Please enter a valid number or 'b' for back.")

            if 0 <= selected_index < len(players):
                return players[selected_index]
            else:
                print("The number is not in the player's number range. Please select another number.")
                return None
                
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return None'''
    
    def _ask_number_choice(self, prompt: str, max_value: int):
        """Utility: ask user for a number within a range."""
        choice = input(prompt).strip().lower()

        if choice == "b":
            return "back"

        if not choice.isdigit():
            print("Please enter a valid number or 'b'.")
            return None

        index = int(choice)
        if 1 <= index <= max_value:
            return index
        else:
            print(f"Please enter a number between 1 and {max_value}.")
            return None

    def _select_players(self, players: list[dict], title: str = "Players: ") -> dict | None:
        """
        Display a list of players and let the user pick one.
        Returns:
            - dict of selected player
            - None if user presses 'b' or invalid selection
        """

        if not players:
            print("There are no players available.")
            return None

        print(f"\n{title}")
        for i, p in enumerate(players, start=1):
            name = p.get("Name", "Unknown")
            handle = p.get("Handle")
            line = f"{i}. {name}"
            if handle:
                line += f" | Handle: {handle}"
            print(line)

        while True:
            choice = input("Enter number (or 'b' to go back): ").strip().lower()

            if choice == "b":
                return None

            if not choice.isdigit():
                print("Please enter a valid number or 'b'.")
                continue

            index = int(choice)

            if 1 <= index <= len(players):
                return players[index - 1]
            else:
                print(f"Please enter a number between 1 and {len(players)}.")



    def _confirm(self, message: str) -> bool:
        answer = input(f"{message} (Y/N)".strip().lower())
        return answer == "y"

    
    def add_to_team(self, team_name: str) -> None:
        '''Captain can add players from the list to his team'''
        player_name = input("Enter the name of the player you want to add to your team: ").strip()
        
        try:
            self.ll_api.add_player_to_team(team_name, player_name)
            print(f"{player_name} has been added to {team_name}.")
        except ValueError as error:
            print("Error: ", error)


    def remove_from_team(self, team_name: str) -> str:
        # get current team members
        players = self.ll_api.get_team_members(team_name)

        if not players:
            print("There are currently no players in your team. Please add members to be able to remove members.")
            return 
        
        player_to_remove = self._select_players(players, "Players in your team: ") # fallið sem velur leikmann
        if not player_to_remove:
            return # if the user pressed b
        
        '''print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get("Name")} | Handle: {p.get("Handle")}")

        try:
            selected = input("Please enter the number of who you want to remove: ")
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return #None
            # return players[selected_index]
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return'''
        
        #player_to_remove = players[selected_index] # eyða

        player_name = player_to_remove.get("Name")

        if not self._confirm(f"Are you sure you want to remove {player_name} from the team?")
           print("Removal cancelled. The player will not be removed from the team.")
           return


        '''confirmation = input(f"Are you sure you want to remove {player_to_remove} from the team? Y/N").strip().lower()
        if confirmation != "y":
            print("Removal cancelled. The player will not be removed from the team.")'''

        try:
            removed_player = self.ll_api.remove_player_from_team(player_to_remove.get("Name"), team_name)
            print(f"{removed_player} has been removed from the team.")
        except ValueError as error:
            print("Error:", error) 


    def cap_see_player_info(self, team_name: str) -> None:
        '''Captain or organizer can see player info'''
        players = self.ll_api.get_team_members(team_name)
        
        if not players:
            print("There are currently no players in your team. Please add members to be able to remove members.")
            return
        
        player_to_see = self._select_players(players, "Select player whose information you want to see: ") # fallið sem velur leikmann
        if not player_to_see:
            return

        '''print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get('Name')}")

        try:
            selected = input("Please enter the number of whose information you want to see: ")
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_see = players[selected_index] # eyða'''

        #player_name = player_to_see.get("Name")

        player_to_see = self._select_players(players, title ="Select player whose information you want to see: ")
        if not player_to_see:
            return
        
        #player_name = player_to_see.get("Name")
        try:
            info = self.ll_api.cap_view_player_info(team_name, player_to_see.get("Name"))
        except ValueError as error:
            print("Error: ", error)

        print(f"\nPlayer Information for {player_to_see}:")
        for attr, value in info.items():
            print(f"{attr}: {value}")


    def select_team_captain(self) -> bool:
        teams = self.ll_api.view_teams()
        if not teams: # If view_teams is empty list
            print("There are no registered teams in the system yet. Please make sure there are registered teams before continuing.")
            return False
        
        print("\nAvailable teams: ")
        for index, team in enumerate(teams, 1):
            print(f"{index}. Team: {team.get('Name')} | Captain: {team.get('Captain')}")

        while True:
            select = self._ask_number_choice("Enter a number for the right team or b to go back:", len(teams))
            if select == "back":
                return False
            if select is None:
                continue

            selected_index = teams[select - 1]
            self.current_team_name = selected_index.get("Name")
            print(f"\nYou are now logged in as captain of {self.current_team_name}")
            return True

    def show_team_members(self):
        if not self._team_is_selected():
            return
        
        players = self.ll_api.get_team_members(self.current_team_name)

        if not players:
            print("There are no players yet in this team.")
            return
        
        print(f"\nPlayers in {self.current_team_name}:")
        for i, p in enumerate(players, 1):
            line = f"{i}. {p.get('Name')}"
            if p.get("Handle"):
                line += f" | Handle: {p.get('Handle')}"
            print(line)

        return players
    

    def show_available_players(self):
        if not self._team_is_selected():
            return
        
        players = self.ll_api.available_players(self.current_team_name)

        if not players:
            print("There are no players available.")
            return
        
        players = sorted(players, key=lambda p: (p.get("Name") or "").lower())

        print("\nAvailable players:")
        for i, p in enumerate(players, 1):
            print(f"{i}. {p.get('Name')}")

        return players


