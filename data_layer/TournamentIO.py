import csv
from Models.Game import Game
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
        results = []
        try:
            with open(GAMES_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 3:
                        score_a = int(row[0]) if row[0] else 0
                        score_b = int(row[1]) if row[1] else 0
                        winner = row[2]
                        results.append(Result(score_a, score_b, winner))
            return results
        except ValueError:
            return "Villa" 

        