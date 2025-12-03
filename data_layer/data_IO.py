#Hér á að koma föll sem ná í rétta data
import csv

PLAYER_PATH: str = r"_data\Players.csv"
TEAM_PATH: str = r"-_data\Teams.csv"
players = []

#Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
class PlayerIO:

    def get_players():
        with open(PLAYER_PATH, "r", encoding="utf-8") as csvfile:
            reader  = csvfile.readlines()
            for row in reader:
                players.append(row)
        return players

    def add_new_player():
        

        pass

    def get_player_stats():
        "sækir tölfræði leikmanna"
        pass

    #Kannski meira    

#Klasi fyrir öllu sem tengist Team í data layerinu sem inheritar model klasan "Team"
class TeamIO:

    def get_team():
        "Sækir í lið til að skoða"
        pass

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