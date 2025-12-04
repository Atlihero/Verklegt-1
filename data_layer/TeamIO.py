import csv

TEAM_PATH: str = r"_data\Teams.csv" #path to the teams csv

class TeamIO:

    def get_team():
        """
        This function creates an empty list and displays the team which was chosen in that list
        """
        try:
            Teams = []
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines()
                for row in reader:
                    Teams.append(row) 
            return Teams 
        except ValueError:
            return f"Error message to be decided"

    def add_new_team(team: list):
        """
        This function is used for creating a new team using csv writer 
        """
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile) 
                writer.writerow(team) 
            return f"New Team added :)"    
        except ValueError:   
            f"Error message to be decided"

    def get_team_stats():
        """
        This function gets two specific stats bu using csv dictreader to search for the right columns(points, wins)
        and then it displays those stats of the selected team
        """
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