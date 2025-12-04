from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO

class Captain_actions():
    
    def add_to_team(self):
        # Input fyrir nafn
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni
        # villa ef reynt er að bæta við manni sem er nú þegar í liði
    
    def remove_from_team(self):
        # input fyrir nafn sem á að eyða úr liðslista
        # warning signs 'u sure u want to delete this person?'
        # villa ef reynt er að taka út leikmann sem er ekki í liðinu

    def see_player_info(self):
        # getur séð allar upplýsingar um leikmenn í sínu liði (eftir að hafa bætt leikmanni í liðið)