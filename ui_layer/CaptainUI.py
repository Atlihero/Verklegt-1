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
        
        Happy_paths.Happy_captain()

        print("\nAvailable captains / teams:")
        for idx, t in enumerate(teams, start=1):
            print(f"{idx}) Captain: {t.captain} | Team: {t.name}")
        
        while True:
            choice = input("Enter captain ID (number) or 'b' to go back: ").strip().lower()

            if choice == "b":
                return False
        
            if not choice.isdigit():
                print("Please enter a number or 'b'.")
                continue

            index = int(choice)
            if 1 <= index <= len(teams):
                selected_team = teams[index - 1]
                self.current_team_name = selected_team.name
                print(f"You are now logged in as captain of team: {self.current_team_name}")
                return True
            
            print(f"Please enter a number between 1 and {len(teams)}.")



    def _get_and_show_team_members(self):
        """get team members for current team"""
        if self.current_team_name is None:
            print("No team selected for this captain.")
            return []
        
        players = self.ll.get_team_members(self.current_team_name)
        
        if not players:
            print("There are currently no players in your team.")
            return []
        
        print("\nPlayers in your team:")
        for index, p in enumerate(players, start = 1):
                name = p.get("Name", "Unkown")
                handle = p.get("Handle", "")
                if handle:
                    print(f"{index}. {name} | Handle: {handle}")
                else:
                    print(f"{index}. {name}")
        return players



    def _get_and_show_avilable_players(self):
        """Show all players that are NOT in any team"""
        if self.current_team_name is None:
            print("No team selected for this captain.")
            return []
        players = self.ll.get_available_players_for_captain(self.current_team_name)
        if not players:
            print("There are no free players to add.")
            return []
        
        # Sort alphabetically by name
        players_sorted = sorted(
            players,
            key=lambda p: (p.get("Name") or "").lower()
        )
        
        print("\nAvailable players (not team yet):")
        for index, p in enumerate(players_sorted, start=1):
            name = p.get("Name", "Unknown")
            print(f"{index}. {name}")
        return players_sorted


    def ensure_team_selected(self) -> bool:
        if self.current_team_name is not None:
            return True
        return self.select_captain_and_team()



    def add_to_team(self):
        '''Captain can add players from the list to his team'''
        if not self.ensure_team_selected():
            return
        
        players = self._get_and_show_avilable_players()
        if not players:
            return
        
        selected = input("Enter the number of the players you want to add (or 'b' for back): ").strip().lower()
        if selected == "b":
            print("Cancelled adding player.")
            return
        
        try:
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the players number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the players number range. Please select another number.")
            return
        
        player_to_add = players[selected_index]
        player_name = player_to_add.get("Name")

        try:
            self.ll.add_player_to_team(self.current_team_name, player_name)
            print(f"{player_name} has been added to {self.current_team_name}.")
        except ValueError as error:
            print("Error:", error)

    def remove_from_team(self):
        if not self.ensure_team_selected():
            return
        

        all_players = self.ll.get_team_members(self.current_team_name)

        # Exclude the captain
        team_list = self.ll.view_teams()
        captain_name = next((t.captain for t in team_list if t.name == self.current_team_name), None)
        
        players = [p for p in all_players if p.get("Name") != captain_name]
        
        if not players:
            print("There are no players to remove ( only the captain exists).")
            return
        
        print(f"\nPlayers in {self.current_team_name} (excluding captain {captain_name}):")
        for index, p in enumerate(players, start=1):
            name = p.get("Name", "Unknown")
            handle = p.get("Handle", "")
            if handle:
                print(f"{index}. {name} | Handle: {handle}")
            else:
                print(f"{index}. {name}")
            


        selected = input("Please enter the number of who you want to remove ( or 'b' for back): ").strip().lower()
        if selected == "b":
            print("Removal cancelled.")
            return


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
        
        players = self._get_and_show_team_members()
        if not players:
            return

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
