import csv
from Models.Game import Game

TOURNAMENT_PATH: str = r"_data/Tournament.csv"
GAMES_PATH: str = r"_data/Games.csv"

class TournamentIO:

    def get_tournaments():
        """
        THis function finds the tournament selected by the user and displayes it for the user
        """
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
        """
        This function is used to create a new tournament by using the csv writer to append this new tournament
        with all its details into the tournament csv file
        """
        try: 
            with open(TOURNAMENT_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tournament) 
            return f"New Tournament added :)"    
        except ValueError: 
            f"Error message to be decided"

    def create_new_game(games: list):
        """
        This function creates a new game for a tournament using the csv writer to append it to the games csv
        """
        try:
            with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(games)
            return f"New Game added"
        except ValueError:
            return "Error"
            
        