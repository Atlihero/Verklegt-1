from logic_layer.LL_api import LL_API

class CaptainUI:
    def __init__(self):
        self.ll = LL_API()


    def add_to_team(self, team_name: str):
        '''Captain can add players from the list to his team'''
        player_name = input("Enter the name of the player you want to add to your team: ")
        try:
            self.ll.add_player_to_team(team_name, player_name)
            print(f"{player_name} has been added to {team_name}.")
        except ValueError as error:
            print("Error: ", error)


    def remove_from_team(self, team_name: str):
        # get current team members
        players = self.ll.get_team_members(team_name)

        if not players:
            print("There are currently no players in your team. Please add members to be able to remove members.")
            return 
        
        print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get("Name")} | Handle: {p.get("Handle")}")

        try:
            selected = input("Please enter the number of who you want to remove: ")
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return
        
        player_to_remove = players[selected_index]

        confirmation = input(f"Are you sure you want to remove {player_to_remove} from the team? Y/N")
        if confirmation.upper() != "y":
            print("Removal cancelled. The player will not be removed from the team.")

        try:
            removed_player = self.ll.remove_player_from_team(player_to_remove.get("Name"), team_name)
            print(f"{removed_player} has been removed from the team.")
        except ValueError as error:
            print("Error:", error) 


    def cap_see_player_info(self, team_name: str):
        '''Captain or organizer can see player info'''
        players = self.ll.get_team_members(team_name)
        if not players:
            print("There are currently no players in your team. Please add members to be able to remove members.")
            return
        
        print("\nPlayers in your team: ")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.get("Name")}")

        try:
            selected = input("Please enter the number of whose information you want to see: ")
            selected_index = int(selected) - 1
            if selected_index < 0 or selected_index >= len(players):
                print("The number is not in the player's number range. Please select another number.")
                return
        except ValueError:
            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_see = players[selected_index]

        try:
            info = self.ll.cap_view_player_info(team_name, player_to_see.get("Name"))
            print(f"\nPlayer Information for {player_to_see}:")
            for attr, value in vars(info).items():
                print(f"{attr}: {value}")
        except ValueError as error:
            print("Error: ", error)


    def organizer_see_info(self):
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
            print(f"\nPlayer Information for {p.get("Name")}:")
            for attr, value in vars(p).items():
                print(f"{attr}: {value}")
            print("-" * 25)