from logic_layer.LL_api import LL_API
from Models.Player import Player

class CaptainUI:
    def __init__(self):
        self.ll = LL_API()
        self.current_team_name: str | None = None

    # Chose which Captain or Team

    def _player_to_dict(self, p: Player) -> dict:
        """Convert Player object to dict so we can comfortably use .get()."""
        return {
            "Name": p.name,
            "DOB": p.dob,
            "Address": p.address,
            "Phonenumber": p.phone,
            "Email": p.email,
            "Handle": p.handle,
            "Team": p.team,
            "Link": p.link,
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
            choice = input("Enter team number to log in as captain: ")

            index = int(choice)
            if 1 <= index <= len(team_names):
                selected_team = team_names[index - 1]
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
        """Show all players that are NOT in any team."""

        players: list[Player] = self.ll.get_available_players_for_captain(
            self.current_team_name
        )
        if not players:
            print("There are no free players to add.")
            return []

        # Sort alphabetically by Name
        players_sorted = sorted(players, key=lambda p: p.name.lower())

        print("\nAvailable players (no team yet):")
        for index, p in enumerate(players_sorted, start=1):
            print(f"{index}. {p.name}")
        return players_sorted





    # Captain actions

    def add_to_team(self):
        '''Captain adds a player that has no team to their team.'''

        players = self._get_and_show_available_players()
        if not players:
            return

        selected = input("Enter the number of the player you want to add: ")

        selected_index = int(selected) - 1
        if selected_index < 0 or selected_index >= len(players):
            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_add = players[selected_index]
        player_name = player_to_add.name

        try:
            self.ll.add_player_to_team(self.current_team_name, player_name)
            print(f"{player_name} has been added to {self.current_team_name}.")
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
            if p.name != captain_name:
                players.append(p)





        if not players:
            print("There are no players to remove (only the captain exists).")
            return





        print(f"\nPlayers in {self.current_team_name} (excluding captain {captain_name}):")
        for index, p in enumerate(players, start=1):
            name = p.name
            handle = p.handle
            print(f"{index}. {name} | Handle: {handle}")


        selected = input("Please enter the number of who you want to remove: ").strip()

        selected_index = int(selected) - 1
        if selected_index < 0 or selected_index >= len(players):
            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_remove = players[selected_index]
        player_name = player_to_remove.name

        confirmation = input(f"Are you sure you want to remove {player_name} from the team? Y/N ").strip().upper()

        if confirmation != "Y":
            print("Removal cancelled. The player will not be removed from the team.")
            return

        try:
            self.ll.remove_player_from_team(self.current_team_name, player_name)
            print(f"{player_name} has been removed from the team.")
        except ValueError as error:
            print("Error:", error)

    def cap_see_player_info(self):
        '''Captain can see detailed info about a player in their own team.'''
        players = self._get_and_show_team_members()


        if not players:

            return


        selected = input("Please enter the number of whose information you want to see: ").strip().lower()

        selected_index = int(selected) - 1
        if selected_index < 0 or selected_index >= len(players):



            print("The number is not in the player's number range. Please select another number.")
            return

        player_to_see = players[selected_index]
        player_name = player_to_see.name

        try:
            player: Player = self.ll.cap_view_player_info(player_name, self.current_team_name)
            info = self._player_to_dict(player)
            print(f"\nPlayer Information for {player_name}:")
            for key, value in info.items():
                print(f"{key}: {value}")

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