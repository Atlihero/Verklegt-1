from Models.Tournament import Tournament
from Models.Round import Round
from data_layer.data_api import DataAPI
import random
from datetime import datetime, timedelta



class LLTournament:
    def __init__(self):
        self.data = DataAPI()
        self.teams = self.data.get_all_teams()

    def create_game(self, tournament_name, round, match_number, match_date, team_a, team_b):
        return [
            tournament_name,
            round,
            match_number,
            match_date,
            team_a,
            team_b,
            None,
            None,
            None
        ]

    def generate_games(self, tournament_name: str, start_date: str):
        if len(self.teams) < 16:
            raise ValueError("You need 16 teams")
        
        if isinstance(start_date, str):
            current_date = datetime.strptime(start_date, "%d/%m/%Y")
        else:
            current_date = start_date 
            
        shuffled = random.sample(self.teams, 16)
        
        rounds = [
            ("R16", 8),
            ("QF", 4),
            ("SF", 2),
            ("F", 1)
        ]

        all_games = []
        match_number = 1

        round_teams = shuffled

        for round, match_count in rounds:
            next_round_teams = ["TBD"] * (match_count)
            for i in range(0, len(round_teams), 2):
                team_a = round_teams[i]
                team_b = round_teams[i + 1]

                match_date = current_date.strftime("%d/%m/%Y")

                game_row = self.create_game(
                    tournament_name = tournament_name,
                    round = round,
                    match_number = match_number,
                    match_date = match_date,
                    team_a = team_a,
                    team_b = team_b
                )
                self.data.new_game(game_row)
                all_games.append(game_row)

                match_number += 1
            
            round_teams = next_round_teams
            
            current_date += timedelta(days=1)

        return all_games
    
    def update_games(self, tournament_name, match_number: int, score_a: int, score_b: int):
        return self.data.update_game(tournament_name, match_number, score_a, score_b)

    def get_all_games(self):
        return self.data.get_games()

    def get_all_tournamnets(self):
        return self.data.get_all_tournaments()
    
    def get_tournament_names(self):
        return self.data.get_tournamentNames()
    
    def advance(self, tournament_name: str, match_number: int, winner: str):
        return self.data.advance_round(tournament_name, match_number, winner)
    

    def new_tourney(self, tournament_obj: Tournament):
        '''want to return as a list, not a dict to have it easier to read'''
        tournament_list = [
            tournament_obj.unique_name,
            tournament_obj.start_date.strftime("%d/%m/%Y"), # takes out the timestamp
            tournament_obj.end_date.strftime("%d/%m/%Y"),
            tournament_obj.venue,
            tournament_obj.contact_person,
            tournament_obj.contact_email,
            tournament_obj.contact_phone
        ]

        return self.data.create_new_tournaments(tournament_list)
