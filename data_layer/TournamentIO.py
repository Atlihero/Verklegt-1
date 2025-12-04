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

    def create_new_game(games: list):
        try:
            with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(games)
            return f"New Game added"
        except ValueError:
            return "Error"

        