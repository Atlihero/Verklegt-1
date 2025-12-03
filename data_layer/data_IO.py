#Hér á að koma föll sem ná í rétta data
import csv

PLAYER_PATH: str = r"_data\Players.csv"
TEAM_PATH: str = r"_data\Teams.csv"

#Klasi fyrir öllu sem tengist player í data layerinu
class PlayerIO:

    def get_players():
        players = []
        with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
            reader  = csvfile.readlines()
            for row in reader:
                players.append(row)
        return players

    def add_new_player(player: list):
        with open(PLAYER_PATH, "a",newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(player)
        return True

    def get_player_stats():
        "sækir tölfræði leikmanna"
        pass

    #Kannski meira    

#Klasi fyrir öllu sem tengist Team í data layerinu sem inheritar model klasan "Team"
class TeamIO:

    def get_team():
        Teams = []
        with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
            reader  = csvfile.readlines()
            for row in reader:
                Teams.append(row)
        return Teams

    def add_new_team():
        "bætir við liði sem user býr til"
        pass

    def get_team_stats():
        "Sækir tölfræði liða"
        pass

    #Kannski meira

class TournamentIO:

    def get_tournaments():
        "Sækir í mót"
        pass

    def add_new_tournament():
        "Bætir við nýju móti"
        pass

    def get_games():
        "Nær í leiki í mótinu !!Líklegt breyting hér!!"
        pass

    def get_round():
        "Nær í rounds í mótinu !!Líklegt breyting hér!!"
    #Kannski meira