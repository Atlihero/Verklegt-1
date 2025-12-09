import csv
from Models.Game import Game

TOURNAMENT_PATH: str = r"data_layer/_data/Tournament.csv"
GAMES_PATH: str = r"data_layer/_data/Games.csv"

class TournamentIO:

    def get_tournaments(self):
        """
        THis function finds the tournament selected by the user and displayes it for the user
        """
        try:
            tournament = []
            with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                reader  = csvfile.readlines() 
                #reader = csv.reader(csvfile) virkar með þessu fyrir Organizer
                for row in reader:
                    tournament.append(row) 
            return tournament 
        except ValueError: 
            return f"Error message to be decided"

    def create_new_tournament(self, tournament: list):
        """
        This function is used to create a new tournament by using the csv writer to append this new tournament
        with all its details into the tournament csv file
        """
        try: 
            with open(TOURNAMENT_PATH, "a",newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(tournament) 
            return f"New Tournament added!"    
        except ValueError: 
            f"Error message to be decided"

    def create_new_game(self, games: list):
        """
        This function creates a new game for a tournament using the csv writer to append it to the games csv
        """
        try:
            with open(GAMES_PATH, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(games)
            return f"New Game added"
        except ValueError:
            return "Error"
            

    def get_all_games(self):
        games = []
        try:
            with open(GAMES_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    games.append(row)
        except FileNotFoundError:
            return []
        return games
    
    def update_games(self, match_number: int, score_a: int, score_b: int):
        games = self.get_all_games()
        winner = None

        update = False
        for game in games:
            if int(game["match_number"]) == match_number:
                game["score_a"] = score_a
                game["score_b"] = score_b

                if score_a > score_b:
                    game["winner"] = game["team_a"]
                
                elif score_b > score_a:
                    game["winner"] = game["team_b"]
                
                else:
                    while score_a == score_b:
                        print("It's a draw. Re-enter the scores:")
                        score_a = int(input(f"Score for {game['team_a']}: "))
                        score_b = int(input(f"Score for {game['team_b']}: "))
                    
                    game["score_a"] = score_a
                    game["score_b"] = score_b
                    game["winner"] = game["team_a"] if score_a > score_b else game["team_b"]

                winner = game["winner"]
                current_round = game["round"]
                tournament_name = game["tournament_name"]
                
                update = True

        if not update:
            return f"No game found"
        
        fieldnames = ["tournament_name","round","match_number","match_date",
                      "team_a","team_b","score_a","score_b","winner"]
        with open(GAMES_PATH, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for g in games:
                writer.writerow(g)
        
        return {"winner": winner, "round": current_round, "tournament_name": tournament_name}

    def advance(self, tournament_name: str, match_number: int, winner: str):
        games = self.get_all_games()

        """
        These are if commands that determine the advance order by match number
        From Round of 16 to QF
        And then from QF to SF
        and then from SF to F
        """
        if 1 <= match_number <= 8:
            next_game = 9 + (match_number - 1) // 2
            slot = "team_a" if match_number % 2 == 1 else "team_b"

        elif 9 <= match_number <= 12:
            next_game = 13 + (match_number - 9) // 2
            slot = "team_a" if match_number % 2 == 1 else "team_b"
        
        elif 13 <= match_number <= 14:
            next_game = 15
            slot = "team_a" if match_number == 13 else "team_b"
        
        else:
            return f"{winner} is the Winner"
        
        for game in games:
            if game["tournament_name"] == tournament_name and int(game["match_number"]) == next_game:
                game[slot] = winner
                break
        
        fieldnames = ["tournament_name","round","match_number","match_date",
                      "team_a","team_b","score_a","score_b","winner"]
        with open(GAMES_PATH, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for g in games:
                writer.writerow(g)
        return f"{winner} advances"

