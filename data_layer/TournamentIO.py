import csv

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
        except ValueError: 
            return f"Error message to be decided"
        return tournament 
    
    def get_tournament_names(self):
        try:
            tournament_names = []
            with open(TOURNAMENT_PATH, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tournament_names.append(row["tournamentName"])
        except FileNotFoundError:
            return "Nothing found"
        return tournament_names

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
    
    def update_game(self, tournament_name: str, match_number: int, score_a: int, score_b: int) -> dict:
        """Updates a game's score and winner. Returns updated game dict or None if not found."""
        games = self.get_all_games()
        updated_game = None

        for game in games:
            if game["tournament_name"] == tournament_name and int(game["match_number"]) == match_number:
                game["score_a"] = score_a
                game["score_b"] = score_b
                if score_a > score_b:
                    game["winner"] = game["team_a"]
                elif score_b > score_a:
                    game["winner"] = game["team_b"]
                else:
                    game["winner"] = None  # Tie handled in logic layer
                updated_game = game
                break

        if updated_game:
            fieldnames = ["tournament_name", "round", "match_number", "match_date",
                          "team_a", "team_b", "score_a", "score_b", "winner"]
            with open(GAMES_PATH, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for g in games:
                    writer.writerow(g)

        return updated_game

    def advance_round(self, tournament_name: str, match_number: int, winner: str) -> bool:
        """Updates the next round with the winner. Returns True if successful."""
        games = self.get_all_games()

        # Determine next game and slot
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
            return False  # Final winner, no next game

        for game in games:
            if game["tournament_name"] == tournament_name and int(game["match_number"]) == next_game:
                game[slot] = winner
                break

        # Write back
        fieldnames = ["tournament_name", "round", "match_number", "match_date",
                      "team_a", "team_b", "score_a", "score_b", "winner"]
        with open(GAMES_PATH, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for g in games:
                writer.writerow(g)

        return True