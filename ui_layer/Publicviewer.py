from logic_layer.LL_api import LL_API
api = LL_API()
class PublicViewer:

    def getplayerPublic(self):
        try:
            userinput = int(input("Veldu ID leikmanns milli 1-48: "))  
            player, team = api.get_playerPublic()

            if userinput < 1 or userinput > len(player):
                print("A player with this id does not exist")
            else:
                print(f"Player: {player[userinput-1]}, Team: {team[userinput-1]}")
        except ValueError:
            print("Please enter a valid integer")


    def getTeamsPublic(self):
        try:
            userinput = int(input("Select team id 1-16: "))
            teams, captain = api.get_teams_public()

            if userinput < 1 or userinput > len(teams):
                print("A team with this ID does not exist")
            else:
                print(f"Team: {teams[userinput-1]}, Captain: {captain[userinput-1]}")
        except ValueError:
            print("Please enter a valid integer")
    
    def view_schedule(title="Current Games"):
        try:
            tournaments = api.get_tournament_names()
            print(tournaments)

            tournament_name = input("Enter tournament name: ").strip()
            if not tournament_name:
                raise ValueError("Tournament name cannot be empty.")
            
            games = api.get_game_by_tournamentName(tournament_name)
            if not games:
                print(f"No games found for tournament: {tournament_name}")
                return []
            
            print(f"\n=== {title} ===")
            for g in games:
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
            
            return games
        
        except ValueError:
            print("Invalid input")



