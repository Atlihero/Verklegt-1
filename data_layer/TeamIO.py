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
        pass