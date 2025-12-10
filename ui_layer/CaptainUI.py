from logic_layer.LL_api import LL_API
from ui_layer.Happy_path import Happy_paths

class CaptainUI:
    def __init__(self):
        self.ll = LL_API()
        self.current_team_name: str | None = None


    def select_captain_and_team(self) -> bool:
        """Ask who the captain is, then find his team"""

        teams = self.ll.view_teams()

        if not teams:
            print("There are no teams in the system yet.")
            return False
        
        print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get('Name')} | Handle: {p.get('Handle')}")

        try:
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return
        
        player_to_remove = players[selected_index]
        player_name = player_to_remove.get("Name", "Unknown")

        confirmation = input(f"Are you sure you want to remove {player_name} from the team? Y/N").strip().upper()
        if confirmation != "Y":
            print("Removal cancelled. The player will not be removed from the team.")
            return

        try:
            self.ll.remove_player_from_team(self.current_team_name, player_name)   
            print(f"{player_name} has been removed from the team.")
        except ValueError as error:
            print("Error:", error) 


    def cap_see_player_info(self):
        '''Captain can see player info for their team members'''

        if not self.ensure_team_selected():
            return
        
        print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get('Name')}")

        selected = input("Please enter the number of whose information you want to see: ")
        if selected == "b":
            return   
        try:
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_see = players[selected_index]
        player_name = player_to_see.get("Name", "Unknown")

        try:
            info = self.ll.cap_view_player_info(player_name, self.current_team_name)
            print(f"\nPlayer Information for {player_name}:")
            for key, value in info.items():
                print(f"{key}: {value}")
        except ValueError as error:
            print("Error: ", error)
