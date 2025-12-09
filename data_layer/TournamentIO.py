import csv
from Models.Game import Game

TOURNAMENT_PATH: str = r"data_layer/_data/Tournament.csv"
GAMES_PATH: str = r"data_layer/_data/Games.csv"

class TournamentIO:

    def get_tournaments():
        try:
            Tournament = []
            with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() 
                for row in reader:
                    Tournament.append(row) 
        except ValueError: 
            return f"Error message to be decided"
        return Tournament 

    def create_new_tournament(self, tournament: list):
        try: 
            with open(TOURNAMENT_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tournament)    
        except ValueError: 
            f"Error message to be decided"
        return f"New Tournament added :)" 

    def create_new_game(self, game_row: list):
        try:
            with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(game_row)
        except ValueError:
            return "Error"
        return f"New Game added"

        