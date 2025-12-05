from logic_layer.LL_api import LL_API


"""
Viewer vill sjá Lið og leikmenn
og þá bara nöfn liða
Handle leikmanns
"""
userinput = int(input("veldu númer leikmanns"))
class PublicViewerUI(LL_API):
     
    def __init__(self):
          super().__init__()
          
    
    def show_all_teams(self):
        teams = self.view_teams()
        return [team["TeamName"] for team in teams]
    
    def show_all_players(self):
         players = self.getplayers()
         return [players]


viewer = PublicViewerUI()
players = viewer.show_all_players()
print(players)
    

     
         