import csv

PLAYER_PATH: str = r"data_layer/_data/Players.csv"

class PlayerIO:

    def get_players(self):
        try:
            players = []
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines()
                for row in reader:
                    print(row)
                    players.append(row)
        except ValueError:
            f"Error message to be decided"
        return players
    

    def get_player_PublicViewer(self):
        try:
            players = []
            team = []
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    players.append(row["Handle"])
                    team.append(row["Team"])
        except ValueError:
            f"Error message"
        return players, team


    def create_new_player(player: list):
        '''Adds player to the csv file'''
        try: 
            with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile) #here the user writes in what is needed for the player like name DOB etc.
                writer.writerow(player) #prints what was written in a new row    
        except ValueError:
            f"Error message to be decided"
        return f"New player added :)"


    def get_player_stats():
        try:
            Points = []
            Handle = []
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Points.append(row["Points"])
                    Handle.append(row["Handle"])
        except ValueError:  #in case of wrong inputs 
            f"Error message to be decided"
        return Handle, Points
