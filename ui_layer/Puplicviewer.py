from logic_layer.LL_api import LL_API


"""
Viewer vill sjá Lið og leikmenn
og þá bara nöfn liða
Handle leikmanns
"""

class PublicViewerUI(LL_API):
     
    def __init__(self):
          super().__init__()
          
    
    def show_all_teams(self):
        teams = self.view_teams()
        return [teams["TeamName"] for team in teams]
    
    def show_team_players(self, team_name):
         team = self.get_teams(team_name)
         if not team:
              return None
         return team.get("player"[]) 
         