import csv

PLAYER_PATH: str = r"_data\Players.csv"

#Class for all the player info 
class PlayerIO:

    def get_players():
        try:
            players = [] #Empty list for the player you are getting
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile: #opens and reads the player.csv
                reader  = csvfile.readlines()   #read the lines in the csv
                for row in reader: #for loop that checks each row
                    players.append(row) #appends the row of the selected input
            return players #returns the "list" for the player that was selected
        except ValueError: #in case of wrong inputs
            f"Error message to be decided"



    def add_new_player(player: list):
        try: 
            with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile) #here the user writes in what is needed for the player like name DOB etc.
                writer.writerow(player) #prints what was written in a new row
            return f"New player added :)"    
        except ValueError:   #in case of wrong inputs 
            f"Error message to be decided"


    def get_player_stats():
        try:
            Points = [] #empty list to be used for storing the points given
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile) #reads the file and 
                for row in reader:
                    Points.append(row["Points"]) #appends the points from the selected player to the list
                return Points
        except ValueError:  #in case of wrong inputs 
            f"Error message to be decided"
        pass