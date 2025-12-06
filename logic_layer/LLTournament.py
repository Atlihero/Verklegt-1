from Models.Tournament import Tournament
from Models.Round import Round
from data_layer.data_api import DataAPI

class Tournament:
    def __init__(self, name: str):
        self.name = name
        self.teams = [
            "Team1", "Team2", "Team3", "Team4",
            "Team5", "Team6", "Team7", "Team8",
            "Team9", "Team10", "Team11", "Team12",
            "Team13", "Team14", "Team15", "Team16"
        ]

    def sum_logic(self, team_name: str) -> int:
        return len(team_name)

    def play_round(self, teams: list[str]) -> list[str]:
        winners = []

        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1]

            score1 = self.sum_logic(team1)
            score2 = self.sum_logic(team2)

            if score1 >= score2:
                winners.append(team1)
            else:
                winners.append(team2)

        return winners

    def run_bracket(self):
        if len(self.teams) != 16:
            raise ValueError("Tournament must have exactly 16 teams")

        left_teams = self.teams[:8]
        right_teams = self.teams[8:]

        # Left side
        r1_left = self.play_round(left_teams)
        r2_left = self.play_round(r1_left)
        r3_left = self.play_round(r2_left)
        champion_left = r3_left[0]

        print(f"Left side champion: {champion_left}")

        # Right side
        r1_right = self.play_round(right_teams)
        r2_right = self.play_round(r1_right)
        r3_right = self.play_round(r2_right)
        champion_right = r3_right[0]

        print(f"Right side champion: {champion_right}")

        # Final
        final = self.play_round([champion_left, champion_right])
        winner = final[0]

        print(f"TOURNAMENT WINNER: {winner}")
        return winner

    def new_tourney(self):
        data = DataAPI()
        return data.new_tournament()
    
    def get_allTournamnets(self):
        data = DataAPI()
        return data.get_all_tournaments()

    
