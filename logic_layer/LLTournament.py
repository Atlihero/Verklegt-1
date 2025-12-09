from Models.Tournament import Tournament
from Models.Round import Round
from data_layer.data_api import DataAPI
import random
from datetime import datetime

class LLTournament:
    def __init__(self):
        self.data = DataAPI()
        self.teams = self.data.get_all_Teams()

    def sum_logic(self, team_name: str) -> int:
        return len(team_name)

    def play_round(self, teams: list[str]) -> list[str]:
        winners = []

        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1]

            score1 = self.sum_logic(team1)
            score2 = self.sum_logic(team2)

            if score1 >= score2:
                winners.append(team1)
            else:
                winners.append(team2)

        return winners

    def run_bracket(self):
        if len(self.teams) != 16:
            raise ValueError("Tournament must have exactly 16 teams")

        left_teams = self.teams[:8]
        right_teams = self.teams[8:]

        # Left side
        r1_left = self.play_round(left_teams)
        r2_left = self.play_round(r1_left)
        r3_left = self.play_round(r2_left)
        champion_left = r3_left[0]

        print(f"Left side champion: {champion_left}")

        # Right side
        r1_right = self.play_round(right_teams)
        r2_right = self.play_round(r1_right)
        r3_right = self.play_round(r2_right)
        champion_right = r3_right[0]

        print(f"Right side champion: {champion_right}")

        # Final
        final = self.play_round([champion_left, champion_right])
        winner = final[0]

        print(f"TOURNAMENT WINNER: {winner}")
        return winner

    def new_tourney(self, tournament_dict: Tournament):
        row = [
            tournament_dict["unique_name"],
            tournament_dict["start_date"],
            tournament_dict["end_date"],
            tournament_dict["venue"],
            tournament_dict["contact_person"],
            tournament_dict["contact_email"],
            tournament_dict["contact_phone"]
        ]
        return self.data.new_tournament(row)

    def add_game(self, game_dict: dict):
        row = [
            game_dict["tournament_name"],
            game_dict["round"],
            game_dict["match_number"],
            game_dict["match_date"],
            game_dict["team_a"],
            game_dict["team_b"],
            game_dict["score_a"],
            game_dict["score_b"],
            game_dict["winner"],
        ]
        return self.data.new_game(row)

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
        
        shuffled = random.sample(self.teams, 16)
        
        rounds = [
            ("R16", 8),
            ("QF", 4),
            ("SF", 2),
            ("F", 1)
        ]

        all_games = []
        match_number = 1
        current_date = datetime.strptime(start_date, "%Y-%m-%d")


        current_teams = shuffled

        for round, match_count in rounds:

            for i in range(0, len(current_teams), 2):
                team_a = current_teams[i]
                team_b = current_teams[i + 1]

                match_date = current_date.strftime("%Y-%m-%d")

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

            current_teams = ["TBD"] * (match_count)

        return all_games
    
    def update_games(self, match_number: int, score_a: int, score_b: int):
        return self.data.update_game(match_number, score_a, score_b)

    def get_all_games(self):
        return self.data.get_games()

    def get_allTournamnets(self):
        return self.data.get_all_tournaments()
    
