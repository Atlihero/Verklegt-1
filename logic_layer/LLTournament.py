from Models.Tournament import Tournament
from data_layer.data_api import DataAPI
import random
from .LLTeams import Team
from .LL_api import LL_API

class LLTournament:
    def __init__(self):
        self.data = DataAPI()
        self.teams = self.data.get_all_Teams()
        self.ll_teams = Team()
        self.lapi = LL_API()
        self.matches =  [] # matches are stored in an empty list
        self.rounds = {}   # rounds are stored

    
    # CONTACT Information 
    def get_contact_info(self, contact:str = "", email:str="", phone : str = ""):
        
        self.contact = contact 
        self.email = email 
        self.phone = phone 


    # Updated Contact Information
    def update_contact_info(self, new_contact: str= "", new_email: str= "", new_phone : str = ""):

        if new_contact:
            self.new_contact = new_contact
        if new_email:
            self.new_email = new_email
        if new_phone:
            self.new_phone = new_phone

    # Scheme of registering a team, a team name cant be twice in one Tournament 
    def register_team(self, team_name: str= "", players : list[str]= None):
        
        if self.lapi.get_teams(team_name) is not None:
            raise ValueError(f"The team {team_name} already exists ")
        
        self.team_name = team_name

        if len(players) < 1: 
            raise ValueError ("A team must have at least 1 player ")
        
        # new team object , not a paramater yk 
        team = team(name=team_name , players = players )
        self.teams.append(team)

        return team 

    # the logic of scheduling games, 
    def schedule_games(self, start_date : str = "", end_date : str =  "", teams : list = 0, venue : str = ""):
        
        self.start_date = start_date 
        self.end_date = end_date 
        self.venue = venue 
        self.teams = teams  

        # requirements to schedule a game  
        if len(teams) < 2 : 
            raise ValueError ("For a match there have to be at least 2 Teams")    
        
        if not start_date:
            raise ValueError ("There is no start date given")
        
        if not end_date: 
            raise ValueError("There is no End Date given")
        
        if not venue : 
            raise ValueError("There is no Venue to be played in")
        
    # records results of games, final score, winner and player ids
    def record_result(self, game_result : int = 0, player_1id : str = "", player_2id : str = "", winner : str = "", outcome : str = "", score : str=  ""):
        self.game_result = game_result
        self.player_1id = player_1id
        self.player_2id = player_2id
        self.winner = winner
        self.outcome = outcome 
        self.score = score 


    # The winner gets printed out 
        if self.winner != "":
            return (f"{self.winner} has won the game!")


    def sum_logic(self, team_name: str) -> int:
        '''checks the length of the team names = strings, 
        it is used for a "fake" scoring system for the def play_round'''
        return len(team_name)


    

    def brackets_of_tournament(self, id : int = 0 , tournamentid : int = 0, type: str= "", totalItems: int = 0, totalRounds: int = 0, status: str = "", ): 
        '''brackets format of the tournament
        16 to 8 to 4 to 2 to 1 (winner!)'''
        self.id = id
        self.tournamentid = tournamentid
        self.type = type
        self.totalItems = totalItems
        self.totalrounds = totalRounds
        self.status = status 

        # checks the amount of teams for the Tournaments
        num_teams = len(self.teams)

        if num_teams < 16 : 
            raise ValueError ("There has to be at least 16 teams in the Tournament. Please enter more teams")
        
        if num_teams % 2!= 0:
            raise ValueError("The number of teams in the tournament must be even.")
        
        # Number of teams in tournament is greater than 16, use power of 2 for team count
        size_of_teams_being_used = [16,32,64]
        if num_teams not in size_of_teams_being_used:
            raise ValueError("The number of teams in the tournament have to be either 16, 32 or 64. Please ")
        

        # Structure of Tournament when it has 16 Teams, get even amount of teams on each side
        if num_teams == 16:
            mid = num_teams // 2 
            left_teams = self.teams[:mid]
            right_teams = self.teams[mid:]

        # Rounds of the teams on the left side
            round1_winners_left = self.play_round(left_teams) 
            round2_winners_left = self.play_round(round1_winners_left)
            round3_winners_left = self.play_round(round2_winners_left)
            champion_left = round3_winners_left[0]
            print(f"The winner from the left side is , {champion_left} !")

        # Rounds of the teams on the right side
            round1_winners_right = self.play_round(right_teams)
            round2_winners_right = self.play_round (round1_winners_right)
            round3_winners_right = self.play_round (round2_winners_right)
            champion_right = round3_winners_right[0]
            print(f"The winner from the right side is , {champion_right}")

        # Final round, 
            finalists = self.play_round([champion_left, champion_right])

            final_winner = finalists[0]
            print(f"The winner of the tournament is, {final_winner}!")
            return final_winner
            
        else:
            current_round = self.teams[:]

        while len(current_round) > 1: 
            current_round = self.play_round(current_round)

        final_winner = current_round[0]
        print(f"The Tournament winner is , {final_winner}!")
        return final_winner


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

        # Rounds of the teams on the left side
        r1_left = self.play_round(left_teams)
        r2_left = self.play_round(r1_left)
        r3_left = self.play_round(r2_left)
        champion_left = r3_left[0]

        print(f"Left side champion: {champion_left}")

        # Rounds of the teams on the right side
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
    
    
    def add_game(self, game_dict: dict):
        row = [
            game_dict["tournament_name"],
            game_dict["round"],
            game_dict["match_number"],
            game_dict["match_date"],
            game_dict["team_a"],
            game_dict["team_b"],
            game_dict["score_a"],
            game_dict["score_b"],
            game_dict["winner"],
        ]
        return self.data.new_game(row)

    def create_game(self, tournament_name, round, match_number, match_date, team_a, team_b):
        return [
            tournament_name,
            round,
            match_number,
            match_date,
            team_a,
            team_b,
            None,
            None,
            None
        ]

    def generate_games(self, tournament_name: str, start_date: str):
        if len(self.teams) < 16:
            raise ValueError("You need 16 teams")
        
        shuffled = random.sample(self.teams, 16)
        
        rounds = [
            ("R16", 8),
            ("QF", 4),
            ("SF", 2),
            ("F", 1)
        ]

        all_games = []
        match_number = 1
        current_date = start_date


        round_teams = shuffled

        for round, match_count in rounds:
            next_round_teams = ["TBD"] * (match_count)
            for i in range(0, len(round_teams), 2):
                team_a = round_teams[i]
                team_b = round_teams[i + 1]

                match_date = current_date.strftime("%d/%m/%Y")

                game_row = self.create_game(
                    tournament_name = tournament_name,
                    round = round,
                    match_number = match_number,
                    match_date = match_date,
                    team_a = team_a,
                    team_b = team_b
                )
                self.data.new_game(game_row)
                all_games.append(game_row)

                match_number += 1
            
            round_teams = next_round_teams

        return all_games
    
    def update_games(self, match_number: int, score_a: int, score_b: int):
        return self.data.update_game(match_number, score_a, score_b)

    def get_all_games(self):
        return self.data.get_games()

    def get_allTournamnets(self):
        return self.data.get_all_tournaments()
    
    def advance(self, tournament_name: str, match_number: int, winner: str):
        return self.data.advance_round(tournament_name, match_number, winner)
    

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

        return self.new_tourney(tournament_list) #fix this shit