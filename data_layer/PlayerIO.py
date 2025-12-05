from Models.Player import Player
import csv
from Models.Player import Player

PLAYER_PATH: str = r"data_layer/_data/Players.csv"

#Class for all the player info 
class PlayerIO:

    def get_players():
        try:
            players = [] #Empty list for the player you are getting
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile: #opens and reads the player.csv
                reader  = csv.reader(csvfile)   #read the lines in the csv
                next(reader, None)
                for row in reader: #for loop that checks each row
                    name, ssn, team = row
                    players.append(Player(name=name, ssn=ssn, team=team)) #appends the row of the selected input
            #return players #returns the "list" for the player that was selected
        except ValueError: #in case of wrong inputs
            f"Error message to be decided"
        return players


    def create_new_player(player: list):
        """
        This functions is used to write a new player into the csv file by using the csv writer
        """
        try: 
            with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile) #here the user writes in what is needed for the player like name DOB etc.
                writer.writerow(player) #prints what was written in a new row
            return f"New player added :)"    
        except ValueError:   #in case of wrong inputs 
            f"Error message to be decided"


    def get_player_stats():
        """
        This function finds the stats of a selected player by using csv dictreader to find the right colum
        and displayes them for the user
        """
        try:
            Points = []
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Points.append(row["Points"])
                return Points
        except ValueError:  #in case of wrong inputs 
            f"Error message to be decided"
        pass