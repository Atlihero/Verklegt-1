import csv
from Models.Player import Player

PLAYER_PATH: str = r"data_layer/_data/Players.csv"
 
class PlayerIO:

    def get_players():
            """
            This function finds the selected player and puts him into an empty list
            to be displayed
            """
            players = [] 
            with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)   
                for row in reader:
                    if not row:
                        continue

                    # If the line is too short then fill with blank
                    if row[0] == "Name":
                        continue
                        
                    name, dob, address, phone, email, handle, team, points = row

                    player = Player(name, dob, address, phone, email, handle, team, points)
                    players.append(player)

            return players
        


    def save_players(players: list[Player]):
        """
        This function takes and saves a player which has been created by using the csv writer to save him
        and he now is in the players csv with all the details he needs
        """
        with open(PLAYER_PATH, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "DOB", "Address", "Phonenumber",
                             "Email", "Handle", "Team", "Points"])
            for p in players:
                writer.writerow([
                    p.name,
                    p.dob,
                    p.address,
                    p.phone,
                    p.email,
                    p.handle,
                    p.team,
                    p.points,
                ])

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