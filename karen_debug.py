from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO
from logic_layer.LLTeams import LLTeams
from logic_layer.LLPlayers import LLPlayer

class Captain_actions():
    
    MAX_TEAM_MEMBERS = 5

    def __init__(self, player_handler : LLPlayer, team_name: str, player_name: str):
        self.llplayerinfo = player_handler
        self.team_name = team_name
        self.player_name = player_name

    def get_team_members(self):
        '''Used to check if team already has 5 players, '''
        all_players = self.llplayerinfo.get_players()
       
        for p in all_players:
            if all_players == self.team_name:
                return p

    bleble = LLTeams.add_player()


    def add():
        # Input fyrir nafn
        # kalla í fallið add_player frá LLTeams klasa
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni - Team is full
        # villa ef reynt er að bæta við manni sem er nú þegar í liði
        pass
    
    def remove_from_team(self):
        
        # input fyrir nafn sem á að eyða úr liðslista
        # warning signs 'u sure u want to delete this person?'
        # villa ef reynt er að taka út leikmann sem er ekki í liðinu
        pass

    def see_player_info(self):
        # getur séð allar upplýsingar um leikmenn í sínu liði (eftir að hafa bætt leikmanni í liðið)
        # setja upp töflu
        pass



    def add_to_team(self):
        name  = input("jakak: ")
        return "are you sure you want to add {name} to your team"
        #need to watch out that a player does not enter twice = done in add_player_to_team
        #player already in another team
        #check if team is full
        #check if player already in
        #call LLteams function

    def remove_from_team(self):
        pass
        #input who do you want to remove
        #check are you sure about this person
        #use function see players in team and make the captain select the player he want to remi
        #LL api has, get_teams 

        #PlayerIO.get_players()
        #player_found = nona


    def see_player_info(self):
        pass
        #open again the fuction to see the players in a team then the captain can select which players information he want to see
        #players. self.get players in team 
        #make new empty list
        #add to that list



#UI layer

# - init -
# add to team = input, corfimation, try except

#remove = input,corfimation, try except

#see player info = print team, format and get info