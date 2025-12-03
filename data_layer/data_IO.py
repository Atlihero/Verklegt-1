#Hér á að koma föll sem ná í rétta data
import csv
from Models.Player import Player
from Models.Team import Team
from Models.Tournament import Tournament
from Models.Game import Game
from Models.Round import Round


PLAYER_PATH: str = "data_layer\_data\Players.csv"

#Klasi fyrir öllu sem tengist player í data layerinu sem inheritar model klasan "player"
class PlayerIO(Player):

    def get_players():
            with open(PLAYER_PATH, "r" , encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row)

    def add_new_player():
        "bætir við leikmanni sem user býr til"
        pass

    def get_player_stats():
        "sækir tölfræði leikmanna"
        pass

    #Kannski meira    

#Klasi fyrir öllu sem tengist Team í data layerinu sem inheritar model klasan "Team"
class TeamIO(Team):

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

class TournamentIO(Tournament, Round, Game):

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