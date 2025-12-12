from .LLPlayers import LLPlayer
from .LLTeams import LLTeams
from .LLTournament import Tournament
from .LLCaptain import LLCaptain
from .LLOrganizer import LLOrganizer
from .LLTournament import LLTournament
from Models.Tournament import Tournament
from Models.Player import Player
from Models.Team import Team
from datetime import datetime


class LL_API:
    def __init__(self):
        self.player = LLPlayer()
        self.team = LLTeams()
        self.tournament = LLTournament()
        self.captain = LLCaptain()
        self.organizer = LLOrganizer()

    
    '''The Logic layer wrapper for the LLPlayer'''

    def get_players_all_off_them(self) -> list:
        '''Gets the players for the organizer to see.'''
        return self.player.get_all_players()
    
    def get_player_public(self) -> list:
        '''Gets the players for the public viewer.'''
        return self.player.get_player_public_viewer()

    def valid_name(self, name: str) -> str:
        '''Validates player's full name.'''
        return self.player.validate_name(name)
    
    def valid_dob(self, dob: str) -> datetime:
        '''Validates player's date of birth.'''
        return self.player.validate_dob(dob)
    
    def valid_address(self, address: str) -> str:
        '''Validates player's address.'''
        return self.player.validate_address(address)
    
    def valid_phone(self, phone: str) -> str:
        '''Validates inputted phone number.'''
        return self.player.validate_phone(phone) 
    
    def valid_email(self, email: str) -> str:
        '''Validates inputted email.'''
        return self.player.validate_email(email)
    
    def valid_handle(self, handle: str) -> str:
        '''Validates the handle of new players.'''
        return self.player.validate_handle(handle)
    
    def validate_link(self, link: str) -> str:
        '''Validates the link of new players.'''
        return self.player.validate_link(link)
    
    def create_player(self, player_obj: Player) -> Player:
        '''Creates a new player.'''
        return self.player.create_player(player_obj)
    

    '''Logic layer wrapper for the LLTeams'''

    def get_teams_public(self) -> list:
        '''Gets the teams for the public viewer to see.'''
        return self.team.get_teams_public()
    
    def add_player(self, team_name: str, player_name: str) -> Player:
        '''Add player to team.'''
        return self.team.add_player_to_team(team_name, player_name)
    
    def get_teams(self, name: str) -> Team | None:
        '''Gets the team by name.'''
        return self.team.get_team_by_name(name)
    
    def check_team(self, name: str) -> bool:
        '''Check if a team already has this name.'''
        return self.team.team_exists(name)

    def add_team(self, name: str, captain: str = None, asciiLogo: str = "") -> Team:
        '''Creates a new team.'''
        return self.team.new_team(name, captain, asciiLogo)

    def select_captains(self, team_name: str, new_captain: str) -> Team:
        '''Selects a new captain for a team.'''
        return self.team.select_captain(team_name, new_captain)

    def view_teams(self) -> list[Team]:
        '''Gets the teams for the public viewer.'''
        return self.team.view_teams() 
    

    '''Logic wrapper for LLTournament'''

    def create_new_game(self, tournament_name: str, round: int, match_number: int, match_date: datetime, team_a: str, team_b: str) -> list:
        '''Creates a game with all attributes needed for a valid game '''
        return self.tournament.create_game(tournament_name, round, match_number, match_date, team_a, team_b)
    
    def generate_games(self, tournament_name: str, start_date: str) -> list:
        '''Makes games for the tournament.'''
        return self.tournament.generate_games(tournament_name, start_date)
    
    def update_game(self, tournament_name: str, match_number: int, score_a: int, score_b: int) -> str:
        '''Updates score of each game that have been played in the tournament.'''       
        return self.tournament.update_games(tournament_name, match_number, score_a, score_b)

    def get_game(self) -> list:
        '''Finds all games in the csv file.'''
        return self.tournament.get_all_games()

    def get_all_tournaments(self) -> list:
        '''List of all tournaments that exist.'''
        return self.tournament.get_all_tournamnets()
    
    def get_tournament_names(self) -> list:
        '''List of all names of tournaments that exist.'''
        return self.tournament.get_tournament_names()

    def advance_round(self, tournament_name: str, match_number: int, winner: str) -> str:
        '''Determines what team advances to the next round of the tournament.'''
        return self.tournament.advance(tournament_name ,match_number, winner)

    def create_new_tournament(self, tournament_obj: Tournament) -> list:
        '''Creates a new tournament in the csv file.'''
        return self.tournament.new_tourney(tournament_obj)
    
    def get_game_by_tournament_name(self, tournament_name) -> list:
        '''Return the games in a tournament'''
        games = self.tournament.get_all_games()
        return [g for g in games if g["tournament_name"] == tournament_name]
    
    def valid_team_name(self, name: str) -> str:
        '''Logic layer wrapper to check team name uniqueness.'''
        return self.team.validate_team_name(name)
    
    
    '''Logic layer wrapper for the LLCaptain'''

    def get_team_members(self, team_name: str) -> list[Player]:
        '''Return a list of players in the team.'''
        return self.captain.get_team_members(team_name)

    def get_available_players_for_captain(self, free_players : str) -> list[Player]:
        '''Shows what players are not in a team'''
        return self.captain.get_available_players(free_players)
    
    def add_player_to_team(self, team_name: str, player_name: str) -> Player:
        '''Captain adds a player to their team.'''
        return self.captain.add_player_to_team(team_name, player_name) 
    
    def remove_player_from_team(self, team_name: str, player_name: str) -> Player:
        '''Captain removes a player from their team.'''
        return self.captain.remove_from_team(player_name, team_name)
    
    def cap_view_player_info(self, player_name: str, team_name: str) -> Player:
        '''Captain can see information on the players in his team.'''
        return self.captain.cap_see_player_info(player_name, team_name)
    
    def update_player_contact(self, player_name: str, team_name: str, new_phone: str, new_address: str, new_email: str) -> Player:
        '''Captain updates a player's phone, address and email.'''
        return self.captain.update_player_contact(player_name, team_name, new_phone, new_address, new_email)
    
    def keep_old_phone(self, new_phone: str, current_phone: str) -> str:
        '''Checks if the user wants to keep their old phone number and not update it'''
        return self.captain.keep_old_phone_number(new_phone, current_phone)
    
    def keep_old_email(self, new_email: str, current_email: str) -> str:
        '''Checks if the user wants to keep their old email address and not update it'''
        return self.captain.keep_old_email(new_email, current_email)
    
    def keep_old_address(self, new_address: str, current_address: str) -> str:
        '''Checks if the user wants to keep their old address and not update it'''
        return self.captain.keep_old_address(new_address, current_address)

    
    def get_team_names_and_captains(self) -> tuple[list[str], list[str]]:
        '''Returns team names and captains for corresponding team'''
        return self.captain.get_names_team_captains()


    '''Logic wrapper for LLOrganizer'''

    def valid_tournament_name(self, name: str) -> str: 
        '''Validates if the tournament name is unique.'''
        return self.organizer.tournament_name(name)
    
    def valid_start_date(self, start_date: str) -> datetime:
        '''Validates if the tournaments start date is in the future.'''
        return self.organizer.choose_start_date(start_date)
    
    def valid_end_date(self, end_date, start_date: str, min_days=5) -> datetime:
        '''Validates if the tournaments end date is later than the start date.'''
        return self.organizer.choose_end_date(end_date, start_date, min_days)
    
    def valid_tournament_location(self, location: str) -> str:
        '''Validates if the tournament has a location.'''
        return self.organizer.tournament_location(location)
    
    def valid_tournament_contact(self, contact_name: str) -> str:
        '''Validates the contact persons name.'''
        return self.organizer.tournament_contact_name(contact_name)

    def organizer_view_player_info(self) -> list:
        '''Organizer can see information about every player in the tournament.'''
        return self.organizer.organizer_player_info()
