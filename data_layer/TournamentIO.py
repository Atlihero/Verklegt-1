import csv
from datetime import datetime
from Models.Result import Result

TOURNAMENT_PATH: str = r"_data\Tournament.csv"
GAMES_PATH: str = r"_data\Games.csv"

class TournamentIO:

    def get_tournaments():
        try:
            Tournament = []
            with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() 
                for row in reader:
                    Tournament.append(row) 
            return Tournament 
        except ValueError: 
            return f"Error message to be decided"

    def create_new_tournament(tournament: list):
        try: 
            with open(TOURNAMENT_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tournament) 
            return f"New Tournament added :)"    
        except ValueError: 
            f"Error message to be decided"

    def get_results():
        Result = []
        try:
            with open(GAMES_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    score_a, score_b, winner = row
                    Result.append(int(score_a), int(score_b), winner)
                return Result
        except ValueError:
            return "Villa kom upp"    
        
    def save_results(result: Result):
        try:
            with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([result.score_A, result.score_B, result.winner])
            return "Results saved"
        except ValueError:
            return "Villa kom upp"
        

        