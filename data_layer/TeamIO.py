import csv

TEAM_PATH: str = r"_data\Teams.csv" 

class TeamIO:

    def get_team():
        try:
            Teams = [] 
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() 
                for row in reader: 
                    Teams.append(row)
            return Teams 
        except ValueError: 
            return f"Error message to be decided"

    def create_new_team(team: list):
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(team)
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