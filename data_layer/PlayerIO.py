import csv
from Models.Player import Player

PLAYER_PATH: str = r"data_layer/_data/Players.csv"
 
class PlayerIO:

    def get_players(self) -> list:
        '''This function finds the selected player and puts him into an empty 
            list to be displayed'''
        players = [] 
        with open(PLAYER_PATH, "r", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)  

            for row in reader:
                if not row and not row.get("Name"): # Skip empty rows that don't have 'name' in the header
                    continue

                if "Link" not in row:
                    row["Link"] = "" # Returns empty if 'link' is not in header
                
                player = Player(
                        row["Name"],
                        row["DOB"],
                        row["Phonenumber"],
                        row["Address"],
                        row["Email"],
                        row["Handle"],
                        row["Team"],
                        row["Link"]
                        ) 
                players.append(player) # Add the newly made player to the players list
        
        return players
    
    
    def get_player_public_viewer(self) -> list:
        '''Shows name and the handle of a player for the publiv viewer'''
        try:
            # Use lists to store each players name and handle and their team
            players = [] 
            team = []
            with open(PLAYER_PATH, "r", encoding = "utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
             
                for row in reader:
                    players.append(row["Handle"])
                    team.append(row["Team"])
                 
        except ValueError:
            f"Failed to display the name and handle of the player. Please try again."
        return players, team


    def save_players(players: list[Player]):
        '''Saves a player which has been created by using the csv writer 
        to save him and is the player now in the csv with all the details needed'''
        with open(PLAYER_PATH, "w", newline = "", encoding = "utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "DOB", "Address", "Phonenumber",
                             "Email", "Handle", "Team", "Link"])
            for p in players:
                writer.writerow([
                    p.name,
                    p.dob,
                    p.address,
                    p.phone,
                    p.email,
                    p.handle,
                    p.team,
                    p.link
                ])


    def create_new_player(player: list):
        '''Used to write a new player into the csv file by using the csv writer'''
        try: 
            with open(PLAYER_PATH, "a",newline = "", encoding = "utf-8") as csvfile:
            # The user writes in what is needed for the player: name, DOB etc.
                writer = csv.writer(csvfile) 
                writer.writerow(player) # Prints what was written in a new row
            return f"New player has been added!"    
        except ValueError:   # In case of wrong inputs 
            f"Failed to add a new player. Please try again."
