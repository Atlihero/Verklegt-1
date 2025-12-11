from logic_layer.LL_api import LL_API
api = LL_API()

class PublicViewer:

    def get_player_public(self):
        try:
            player, team = api.get_player_public() # Get list of players and their team

            while True:
                try: 
                    userinput = int(input(f"Select a player ID between 1-{len(player)}: "))
                
                    if 1 <= userinput <= len(player): # Check if the input is valid
                        break
                    else:
                        print("A player with this ID number does not exist")

                except ValueError:
                    print("The input has to be a integer number. Please enter a valid number.")
                        
            print(f"Player: {player[userinput-1]}, Team: {team[userinput-1]}") # Show the player and its team
        
        except ValueError as error:
            print("Please enter a valid integer")


    def get_teams_public(self):
        try:
            teams, captain = api.get_teams_public() # Get list of teams and their captains
            
            while True:
                try:
                    userinput = int(input(f"Select team ID between 1-{len(teams)}: "))

                    if 1 <= userinput <= len(teams): # Check if the input is valid
                        break
                    else:
                        print("A team with this ID does not exist")

                except ValueError:
                    print("please enter a valid integer")

            print(f"Team: {teams[userinput-1]}, Captain: {captain[userinput-1]}") # Show team and its captain

        except ValueError:
            print("Please enter a valid integer")
    

def view_schedule(title="Current Games"):
        try:
            tournaments = api.get_tournament_names() # Gets all tournament names
            print(tournaments)
            
            while True:
                tournament_name = input("Enter tournament name: ").strip()

                if tournament_name in tournaments: # Confirms that the tournament is in the system
                    break

                print("Tournament not found. Please enter a valid tournament name.")
            
            # Get all games/matches that are in the tournament 
            games = api.get_game_by_tournament_name(tournament_name) 

            if not games: # If there are no games found
                print(f"No games found for tournament: {tournament_name}")
                return []
            
            print(f"\n=== {title} ===")
            for g in games: # Print information on every match/game
                print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                    f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
            
            return games
        
        except ValueError:
            print("Invalid input")
