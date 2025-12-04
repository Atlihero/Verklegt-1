from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO
from logic_layer.LLTeams import LLTeams
from LLPlayers import LLPlayer

class Captain_actions():
    
    MAX_TEAM_MEMBERS = 5

    def __init__(self, player_handler : LLPlayer, team_name: str, player_name: str):
        self.llplayerinfo = player_handler
        self.team_name = team_name
        self.player_name = player_name

    def get_team_members(self):
        '''Used to check if team already has 5 players, '''
        all_players = self.llplayerinfo.get_players()
        all_players = PlayerIO.get_players()
        for p in all_players:
            if all_players == self.team_name:
                return p

    bleble = LLTeams.add_player()


       
        # Input fyrir nafn
        # kalla í fallið add_player frá LLTeams klasa
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni - Team is full
        # villa ef reynt er að bæta við manni sem er nú þegar í liði
    
    def remove_from_team(self):
        remove_player = input("Please enter the name of the player you want to remove: ")
        # input fyrir nafn sem á að eyða úr liðslista
        # warning signs 'u sure u want to delete this person?'
        # villa ef reynt er að taka út leikmann sem er ekki í liðinu
        pass

    def see_player_info(self):
        # getur séð allar upplýsingar um leikmenn í sínu liði (eftir að hafa bætt leikmanni í liðið)
        # setja upp töflu
        pass