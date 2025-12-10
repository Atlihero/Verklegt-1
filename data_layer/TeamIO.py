import csv

TEAM_PATH: str = r"data_layer/_data/Teams.csv" # Path to the teams csv

class TeamIO:

    def get_team(self) -> list:
        '''Returns a list of players for a specific team'''
        try:
            teams = [] # Empty list in which the team that is chosen goes into
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() # Reads the linse in the csv
                for row in reader: # For loop that goes through the lines to look for the right team
                    teams.append(row) # Append the team chosen to the list
            return teams # Returns the list
        except ValueError: # In case of wrong inputs
            f"It was not possible to return a new list of players for the team. Please try again."
        return teams # Returns the list
    

    def getTeam_public(self) -> list:
        '''Only shows captain and team name for the public viewer '''
        try:
            teams = [] 
            captain = []
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    teams.append(row["TeamName"])
                    captain.append(row["Captain"])
        except ValueError:
            f"Failed to display the captain and the team name. Please try again."
        return teams, captain
    

    def get_team_stats(self) -> list:
        '''Gathers wins and points for a team and puts in a list for easy access'''
        try:
            Wins = [] # Empty list for the wins of teams
            Points = [] # Empty list for the points of teams
            with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile) #reads the file like a dictionary
                for row in reader: 
                # Adds the wins to wins list based on the number in the wins column in the csv
                    Wins.append(row["Wins"]) 
                # Adds the points to points list based on the number in the points column in the csv
                    Points.append(row["Points"]) 
                return Wins, Points # Returns both of those lists with updated numbers
        except ValueError:  # In case of wrong inputs 
            f"Failed to display the points and wins of the team. Please try again."
        pass
        

    def create_new_team(self, name: str, captain: str = None, asciiLogo: str = "") -> str:
        '''create an empty team with no players'''
        try: 
            with open(TEAM_PATH, "a",newline="", encoding="utf-8") as csvfile:
        # The user writes in the details needed for a team like the name
                writer = csv.writer(csvfile) 
                writer.writerow([name, captain, asciiLogo]) # Prints what was written in a new row 
        except ValueError: # In case of wrong inputs 
            f"Failed to add a new team. Please try again."
        return f"New team has been added!" 


    def add_teams_to_tournament(tournament: str, teams: list) -> str:
        '''Organizer will use to add teams to a designated tournament'''
        if len(teams) != 16:
            return "Error, not enough teams in the tournament. There have to be at least 16 teams."
        try:
            with open(TEAM_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                for team in teams:
                    writer.writerow([tournament, team])
                return "The team has been added to the tournament."
        except ValueError:
            return "Failed to add the team to the tournament. Please try again."


    def get_team_wins_points(team_name: str) -> str:
        '''Finds wins and points for a team'''
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
                
        raise ValueError("Team was not found in Teams.csv file. Please try again.")
        

    def get_all_teams(self) -> list:
        '''returns a list of all team names'''
        teams: list = []
        try:
            with open(TEAM_PATH, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        teams.append(row[0])
        except FileNotFoundError:
            f"The file was not found" 
            pass
        return teams