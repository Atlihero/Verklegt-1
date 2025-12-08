import csv

TEAM_PATH: str = r"data_layer/_data/Teams.csv" #path to the teams csv

class TeamIO:

    def get_team():
        '''returns a list of players for a specific team'''
        try:
            Teams = [] #Empty list in which the team that is chosen goes into
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() #reads the linse in the csv
                for row in reader: #for loop that goes through the lines to look for the right team
                    Teams.append(row) #append the team chosen to the list
        except ValueError: #in case of wrong inputs
            return f"Error message to be decided"
        return Teams #returns the list
        
    def getTeam_public(self):
        try:
            teams = []
            captain = []
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    teams.append(row["TeamName"])
                    captain.append(row["Captain"])
        except ValueError:
            f"error message"
        return teams, captain

    def _new_team(team: list):
        '''create an empty team with no players'''
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile) #here the user writes in the details needed for a team like the name
                writer.writerow(team) #prints what was written in a new row
            return f"New Team added :)"    
        except ValueError:   #in case of wrong inputs 
            f"Error message to be decided"

    def get_team_stats():
        try:
            Wins = [] #empty list for the wins of teams
            Points = [] #empty list for the points of teams
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile) #reads the file like a dictionary
                for row in reader: 
                    Wins.append(row["Wins"]) #adds the wins to the wins list based on the number in the wins column in the csv
                    Points.append(row["Points"]) #adds the points to the points list based on the number in the points column in the csv
                return Wins, Points #returns both of those lists and now 
        except ValueError:  #in case of wrong inputs 
            f"Error message to be decided"
        pass
        
    def add_teams_to_tournament(tournament: str, teams: list):
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
        
    def get_team_wins_points(team_name: str):
        """Finds wins and points for a team"""

        with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # skip header

            for row in reader:
                # row = [TeamID, TeamName, Captain, Wins, Points]
                if len(row) < 5:
                    continue

                name = row[1].strip('"')

                if name == team_name:
                    wins = int(row[3])
                    points = int(row[4])
                    return wins, points
        
        raise ValueError("Team was not found in Teams.csv")

    def get_all_teams() -> list:
            '''returns a list of all team names'''
            teams: list = []
            try:
                with open(TEAM_PATH, "a", newline="", encoding="utf-8") as csvfile:
                #with open(TEAM_PATH, "r", newline="", encoding="utf-8") as csvfile: þetta virkar fyrir OrganizerUI
                    reader = csv.writer(csvfile)
                    #reader = csv.reader(csvfile)
                    for row in reader:
                        if row:
                            teams.append(row[0])
            except FileNotFoundError:
                pass
            return teams