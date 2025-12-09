from Models.Tournament import Tournament
from data_layer.data_api import DataAPI
from datetime import datetime
from data_layer.TournamentIO import TournamentIO


class LLTournament:
    
    def __init__(self):
        self.data = DataAPI()
        self.teams = self.data.get_all_Teams()
        self.tournamentio = TournamentIO()

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
    

    def new_tourney(self, tournament_obj: Tournament):
        '''want to return as a list, not a dict to have it easier to read'''
        tournament_list = [
            tournament_obj.unique_name,
            tournament_obj.start_date.strftime("%d/%m/%Y"), # takes out the timestamp
            tournament_obj.end_date.strftime("%d/%m/%Y"),
            tournament_obj.venue,
            tournament_obj.contact_person,
            tournament_obj.contact_email,
            tournament_obj.contact_phone
        ]

        return self.tournamentio.create_new_tournament(tournament_list)
    
    
    def get_allTournaments(self):
        return self.data.get_all_tournaments()