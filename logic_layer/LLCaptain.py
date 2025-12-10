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
        """Get all players as Player objects."""
        return self.data_api.get_all_players() or []


    def _player_to_dict(self, p: Player) -> dict:
        """Convert a Player object to a dict"""
        return{
                "Name": getattr(p, "name", ""),
                "DOB": getattr(p, "dob", ""),
                "Address": getattr(p, "address", ""),
                "Phonenumber": getattr(p, "phone", ""),
                "Email": getattr(p, "email", ""),
                "Handle": getattr(p, "handle", ""),
                "Team": getattr(p, "team", ""),

        }



        

    def get_team_members(self, team_name: str) -> list[dict]:
        '''Check if players are in this team and return a list of members dicts'''
        team_name = (team_name or "").strip()
        all_players = self._get_all_players()
        

        team_players: list[Player] = [
            p for p in all_players
            if  (getattr(p,"team", "") or "").strip() == team_name
        ]
        return [self._player_to_dict(p) for p in team_players]
    
    def get_available_players(self, team_name: str) -> list[dict]:
        '''Return players that do not belong to any team'''
        all_players = self._get_all_players()
        
        free_players: list[Player] =  [
            p for p in all_players
            if not ((getattr(p, "team", "") or "").strip())
        ]

        return [self._player_to_dict(p) for p in free_players]

    
    def add_player_to_team(self, team_name: str, player_name: str) -> dict:
        '''Used to check if team already has 5 players, '''

        team_name = (team_name or "").strip()
        player_name = (player_name or "").strip()

        #team_players = self.get_team_members(team_name)
        team = self.ll_teams.get_team_by_name(team_name)
        if team is None:
            raise ValueError("Team not found")
        

        all_players = self._get_all_players()

        team_players = [
            p for p in all_players
            if (getattr(p, "team", "") or "").strip() == team_name
        ]
        if len(team_players) >= self.MAX_TEAM_MEMBERS:
            raise ValueError ("There are already 5 players in this team.")
       

        player_to_add: Player | None = None
        for p in all_players:
            if (getattr(p, "name", "") or "").strip() == player_name:
                player_to_add = p
                break

        if player_to_add is None:
            raise ValueError("Player not found.")

        # Check if player is already in another team
        current_team = (getattr(player_to_add, "team","") or "").strip()
        if current_team not in ("", team_name):
            raise ValueError(f"{player_name} is already in another team.")
        
        # Add player to this team
        player_to_add.team = team_name

        # Save changes
        PlayerIO.save_players(all_players)
        return self._player_to_dict(player_to_add)
    
    
    def remove_from_team(self, player_name: str, team_name: str) -> dict:
        '''Allows captain to remove a player from team'''
        player_name = (player_name or "").strip()
        team_name = (team_name or "").strip()

        all_players = self._get_all_players()
        player_found: Player | None = None

        for p in all_players:
            if (getattr(p, "name", "") or "").strip() == player_name:
                player_found = p
                break
                    
        if player_found is None:
            raise ValueError ("This player does not exist. Please try another player.")
        
        if (getattr(player_found, "team", "") or "").strip() != team_name:
            raise ValueError ("The player is not in this team. Please try another player.")
    
        player_found.team = ""

        PlayerIO.save_players(all_players)
        return self._player_to_dict(player_found)
    

    def cap_see_player_info(self, player_name: str, team_name: str) -> dict:
        '''Allows captains to see the players info that are on their team'''
        player_name = (player_name or "").strip()
        team_name = (team_name or "").strip()

        all_players  =self._get_all_players()

        for p in all_players:
            if ((getattr(p, "name", "") or "").strip() == player_name and
                (getattr(p, "team", "") or "").strip() == team_name):
                return self._player_to_dict(p)
            
            #if player not found in the team
        raise ValueError("Player is not in this team. Please try another player.")
        

    def update_player_contact(
            self,
            player_name: str,
            team_name: str,
            new_phone: str,
            new_address: str,
            new_email: str,
    ) -> dict:


        '''Update phone, address and email for a player in a team.'''
        player_name = (player_name or "").strip()
        team_name = (team_name or "").strip()

        all_players = self._get_all_players()
        player: Player | None = None

        # Find the player in this team
        for p in all_players:
            name = (getattr(p, "name", "") or "").strip()
            team = (getattr(p, "team", "") or "").strip()
            if name == player_name and team == team_name:
                player = p
                break

        if player is None:
            raise ValueError("Player is not in this team. Please try another player.")
            
        # Only update field if the captain actually typed something
        if new_phone.strip() != "":
            player.phone = new_phone.strip()

        if new_address.strip() != "":
            player.address = new_address.strip()

        if new_email.strip() != "":
            player.email = new_email.strip()

        # Save all players back to csv
        PlayerIO.save_players(all_players)

        # Return update info as dict
        return self._player_to_dict(player)