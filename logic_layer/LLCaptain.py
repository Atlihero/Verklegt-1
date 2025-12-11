from data_layer.PlayerIO import PlayerIO
from logic_layer.LLTeams import LLTeams
from data_layer.data_api import DataAPI
from Models.Player import Player


class LLCaptain():
    
    MAX_TEAM_MEMBERS = 5

    def __init__(self):
        self.ll_teams = LLTeams()
        self.data_api = DataAPI()

    def _get_all_players(self) -> list[Player]:
        '''Get all players as Player objects.'''
        return self.data_api.get_all_players() or []

    def get_team_members(self, team_name: str) -> list[Player]:
        '''Return Player objects that belong to this team.'''
        team_name = team_name.strip()
        all_players = self._get_all_players()
        
        team_players: list[Player] = []

        for player in all_players:
            team = player.team.strip()
            if team == team_name:
                team_players.append(player)

        return team_players

    
    def get_available_players(self, team_name: str) -> list[Player]:
        '''Return players that do not belong to any team'''
        all_players = self._get_all_players()
        
        free_players: list[Player] = []

        for player in all_players:
            team = player.team.strip()
            if not team:
                free_players.append(player)

        return free_players


    
    def add_player_to_team(self, team_name: str, player_name: str) -> Player:
        '''Captain adds a player to his team'''

        team_name = team_name.strip()
        player_name = player_name.strip()

        team = self.ll_teams.get_team_by_name(team_name)
        if team is None:
            raise ValueError("Team not found")
        

        all_players = self._get_all_players()

        team_players = self.get_team_members(team_name)



        if len(team_players) >= self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       

        player_to_add: Player | None = None
        for player in all_players:
            name = player.name.strip()
            if name == player_name:
                player_to_add = player
                break

        if player_to_add is None:
            raise ValueError("Player not found.")


        # Check if player is already in another team
        current_team = player_to_add.team.strip()
        if current_team not in ("", team_name):
            raise ValueError(f"{player_name} is already in another team.")

        
        # Add player to this team
        player_to_add.team = team_name

        # Save changes
        PlayerIO.save_players(all_players)
        return player_to_add
    
    
    def remove_from_team(self, player_name: str, team_name: str) -> Player:
        '''Allows captain to remove a player from team'''

        player_name = player_name.strip()
        team_name = team_name.strip()

        all_players = self._get_all_players()
        player_found: Player | None = None

        for player in all_players:
            name = player.name.strip()
            if name == player_name:
                player_found = player
                break

                    
        if player_found is None:
            raise ValueError ("This player does not exist. Please try another player.")
        
        team = player_found.team.strip()
        if team != team_name:
            raise ValueError("The player is not in this team. Please try another player.")

        player_found.team = ""

        PlayerIO.save_players(all_players)
        return player_found
    

    def cap_see_player_info(self, player_name: str, team_name: str) -> Player:
        """Allows captains to see the players info that are on their team."""

        player_name = player_name.strip()
        team_name = team_name.strip()

        all_players = self._get_all_players()

        # Find the player in this team
        for p in all_players:
            name = p.name.strip()
            team = (p.team or "").strip()

            if name == player_name and team == team_name:
                return p

        # if we finish the loop without returning, player wasn't found in this team
        raise ValueError("Player is not in this team. Please try another player.")

        

    def update_player_contact(
            self,
            player_name: str,
            team_name: str,
            new_phone: str,
            new_address: str,
            new_email: str,
        ) -> Player:


        '''Update phone, address and email for a player in a team.'''
        player_name = player_name.strip()
        team_name = team_name.strip()

        all_players = self._get_all_players()
        player: Player | None = None

        # Find the player in this team
        for p in all_players:
            if p.name == player_name and p.team == team_name:
                player = p
                break



        if player is None:
            raise ValueError("Player is not in this team. Please try another player.")
            
        # Only update field if the captain typed something
        if new_phone.strip() != "":
            player.phone = new_phone.strip()

        if new_address.strip() != "":
            player.address = new_address.strip()

        if new_email.strip() != "":
            player.email = new_email.strip()

        # Save all players back to csv
        PlayerIO.save_players(all_players)
        return player