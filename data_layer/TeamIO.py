import csv
import sys

#TEAM_PATH: str = r"_data\Teams.csv" 
TEAM_PATH = "data_layer/_data/Teams.csv"
#my_file = open(sys.path[0]+"/"+COUNTRIES_OF_THE_WORLD, "r")
class TeamIO:

    def get_team():
        '''returns a list of players for a specific team'''
        try:
            Teams = [] 
            with open(sys.path[0]+"/"+TEAM_PATH, "r") as csvfile:
            #with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() 
                for row in reader: 
                    Teams.append(row)
            return Teams 
        except ValueError: 
            return f"Error message to be decided"

    def create_new_team(team_name: list):
        '''create an empty team with no players'''
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(team_name)
            return f"New Team added :)"    
        except ValueError:
            f"Error message to be decided"

    def get_team_stats():
        try:
            Wins = []
            Points = []
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader: 
                    Wins.append(row["Wins"])
                    Points.append(row["Points"])
                return Wins, Points 
        except ValueError:
            f"Error message to be decided"
        
    def add_teams_to_tournament(tournament: str, teams: list):
        if len(teams) != 16:
            return "Villa ekki eru 16 lið í mótinu"
        try:
            with open(TEAM_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                for team in teams:
                    writer.writerow([tournament], team)
                return "Teams added"
        except ValueError:
            return "Villa eittvhað fór úsrkeiðis"
        

    def get_all_teams() -> list:
        '''returns a list of all team names'''
        teams: list = []
        try:
            with open(TEAM_PATH, "a", newline="", encoding="utf-8") as csvfile:
                reader = csv.writer(csvfile)
                for row in reader:
                    if row:
                        teams.append(row[0])
        except FileNotFoundError:
            pass
        return teams
