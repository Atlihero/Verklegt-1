from logic_layer.LL_API import LL_API
# from logic_layer.LLPlayers import LLPlayer
# from logic_layer.LLTeams import LLTeams
# from logic_layer.LLCaptain import LLCaptain


class CaptainUI:
    def __init__(self, LLPlayers, LLTeams):
        self.players = LLPlayers
        self.teams = LLTeams
        self.ll = LL_API()

    # def add_player(self, p):
    #     self.players.add_player(p)

    # def add_team(self, t):
    #     self.teams.create_team(t)


    def add_to_team(self):
        pass
        input ("Who do you want to add to your team?")
        # Input fyrir nafn
        # kalla í fallið add_player frá LLTeams klasa
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni - Team is full
        # villa ef reynt er að bæta við manni sem er nú þegar í liði


    def remove_from_team(self, team_name: str):
        pass
        # get current team members
        players = self.ll.get_team_members(team_name)

        if not players:
            print("There are no players currently in your team. Please add members to be able to remove members.")
            return 
        
        print("\nPlayers in your team")
        for index, p in enumerate(start = 1):
            print(f"{index}. {p.name} | Handle: {p.handle}")

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
            removed_player = self.ll.remove_from_team(player_to_remove.name, team_name)
            print(f"{removed_player} has been removed from the team.")
        except ValueError as error:
            print("Error:", error) 

    def see_player_info(self):
        pass
        input("Choose whose information you want to see.") # setja i menuUI