from logic_layer.LL_api import LL_API
api = LL_API()
class PublicViewer:

    def getplayerPublic(self):
        try:
            player, team = api.get_playerPublic()

            while True:
                try:
                    userinput = int(input(f"Select a player id between 1-{len(player)}: "))

                    if 1 < userinput <= len(player):
                        break
                    else:
                        print("A player with this id does not exist")
                except ValueError:
                    print("please enter a valid integer")
                        
            print(f"Player: {player[userinput-1]}, Team: {team[userinput-1]}")
        except ValueError as e:
            print("Please enter a valid integer")


    def getTeamsPublic(self):
        try:
            teams, captain = api.get_teams_public()
            
            while True:
                try:
                    userinput = int(input(f"Select team id between 1-{len(teams)}: "))

                    if 1 < userinput <= len(teams):
                        break
                    else:
                        print("A team with this id does not exist")
                except ValueError:
                    print("please enter a valid integer")

            print(f"Team: {teams[userinput-1]}, Captain: {captain[userinput-1]}")

        except ValueError:
            print("Please enter a valid integer")
    
    def view_schedule(title="Current Games"):
        try:
            tournaments = api.get_tournament_names()
            print(tournaments)
            
            while True:
                tournament_name = input("Enter tournament name: ").strip()

                if tournament_name in tournaments:
                    break

                print("Tournament not found. Please enter a valid tournament name.")
            
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



