import csv

"path to the teams csv file"
TEAM_PATH: str = r"_data/Teams.csv" 

class TeamIO:

    def get_team():
        '''
        This function finds the team which was selected by reading through the lines in the csv
        and add it to a empty list which is then pulled up and displayed
        '''
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
        '''
        this function adds a team to the csv by putting the inputs into the csv writer
        which then add the new team with all the details into the csv file
        '''
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(team)
            return f"New Team added :)"    
        except ValueError: 
            f"Error message to be decided"

    def get_team_stats():
        """
        This function reads through the team csv path for the inputted team and puts the wins and points stats
        of the team selected into a list which is to be dislpayed
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
        pass
        
    def add_teams_to_tournament(tournament: str, teams: list):
        """
        This function adds teams to the tournament and if by using the csv writer
        And if there are not 16 teams in the tournament it displayes an error message
        """
        if len(teams) != 16:
            return "Error, not enough teams in the tournament. There has to be 16 teams."
        try:
            with open(TEAM_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                for team in teams:
                    writer.writerow([tournament, team])
                return "Teams added"
        except ValueError:
            return "Villa eittvhað fór úsrkeiðis"

    def get_all_teams() -> list:
            '''returns a list of all team names in a newline'''
            teams = []
            try:
                with open(TEAM_PATH, "r", newline="", encoding="utf-8") as csvfile:
                    reader = csv.writer(csvfile)
                    for row in reader:
                        if row:
                            teams.append(row[0])
            except FileNotFoundError:
                pass
            return teams
