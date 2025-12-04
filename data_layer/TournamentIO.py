import csv

TOURNAMENT_PATH: str = r"_data\Tournament.csv"

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

    def add_new_tournament(tournament: list):
        try: 
            with open(TOURNAMENT_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tournament) 
            return f"New Team added :)"    
        except ValueError: 
            f"Error message to be decided"
        

    def add_teams_to_tournament():

        pass

    def get_round():
        "Nær í rounds í mótinu !!Líklegt breyting hér!!"
        pass