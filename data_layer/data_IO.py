#Hér á að koma föll sem ná í rétta data
import csv

#Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
class PlayerIO:
    def get_players():
        "sækir í leikmenn til að skoða"
        pass

    def add_new_player():
        "bætir við leikmanni sem user býr til"
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