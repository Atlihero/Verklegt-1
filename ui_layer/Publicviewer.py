from logic_layer.LL_api import LL_API
api = LL_API()
class PublicViewer:
    
    def getplayerPublic(self):
        userinput = int(input("Veldu ID leikmanns milli 1-48: "))  
        player, team = api.get_playerPublic()
        print(f"Player: {player[userinput-1]}, Team: {team[userinput-1]}")


    def getTeamsPublic(self):
        userinput = int(input("Select team id 1-16: "))
        teams, captain = api.get_teams_public()
        print(f"Team: {teams[userinput-1]}, Captain: {captain[userinput-1]}")
    
    def view_schedule(title="Current Games"):
        tournaments = api.get_tournament_names()
        print(tournaments)

        tournament_name = input("Enter tournament name: ").strip()
        games = api.get_game_by_tournamentName(tournament_name)
        
        print(f"\n=== {title} ===")
        for g in games:
            print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
        
        return games



