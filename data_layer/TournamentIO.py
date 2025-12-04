import csv

TOURNAMENT_PATH: str = r"_data\Tournament.csv"

class TournamentIO:

    def get_tournaments():
        try:
            Tournament = [] #Empty list in which the tournament that is chosen goes into
            with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() #reads the lines in the csv
                for row in reader: #for loop that goes through the lines to look for the right tournament
                    Tournament.append(row) #append the tournament chosen to the list
            return Tournament #returns the list
        except ValueError: #in case of wrong inputs
            return f"Error message to be decided"

    def add_new_tournament():
        "Bætir við nýju móti"
        pass

    def add_teams_to_tournament():
        pass

    def get_games():
        "Nær í leiki í mótinu !!Líklegt breyting hér!!"
        pass

    def get_round():
        "Nær í rounds í mótinu !!Líklegt breyting hér!!"