class LLTournament():

    #16 teams in the tournament
    def __init__(self, name : str ):
        self.tournament = name
        self._next_game_id  = 1
        self.teams = [ "Team1" , "Team2", "Team3 ", "Team4", "Team5", "Team6", "Team7", "Team8", 
                    "Team9", "Team10", "Team11", "Team12", "Team13", "Team14", "Team15", "Team16"]


    def get_contact_info(self, contact:str = "", email:str="", phone : str = ""):
        '''Contact information'''
        self.contact = contact 
        self.email = email 
        self.phone = phone 


    def update_contact_info(self, new_contact: str= "", new_email: str= "", new_phone : str = ""):
        '''Updated contact information'''
        if new_contact:
            self.new_contact = new_contact
        if new_email:
            self.new_email = new_email
        if new_phone:
            self.new_phone = new_phone


    def register_team(self, team_name: str= "", players : list[str]= None):
        '''Scheme of registering a team, a team name cant be twice in one Tournament '''
        if self.find.team.by_name(team_name) is not None:
            raise ValueError(f"The team {team_name} already exists ")
        
        self.team_name = team_name

        if len(players) < 1: 
            raise ValueError ("A team must have at least 1 player ")
        
        # new team object , not a paramater yk 
        team = team(name=team_name , players = players)
        self.tournament.teams.append(team)
        return team 

    # the logic of scheduling games, 
    def schedule_games(self, start_date : str = "", end_date : str =  "", teams : list = 0, venue : str = ""):
        '''The logic of scheduling games'''
        self.start_date = start_date 
        self.end_date = end_date 
        self.venue = venue 
        self.teams = teams 

        # store all matches in a empty list 
        self.matches =  [] # matches are stored 
        self.rounds = {} # rounds are stored 

        # requirements to schedule a game  
        if len(teams) < 2 : 
            raise ValueError ("For a match there have to be at least 2 Teams. Please enter teams for the match.")    
        
        if not start_date:
            raise ValueError ("There is no start date given. Please enter a start date.")
        
        if not end_date: 
            raise ValueError("There is no End Date given. Please enter a end date.")
        
        if not venue : 
            raise ValueError("There is no Venue to be played in. Please enter a venue location.")

    
    def record_result(self, game_result : int = 0, player_1id : str = "", player_2id : str = "", winner : str = "", outcome : str = "", score : str=  ""):
        '''Records results of games, final score, winner and player ids'''
        self.game_result = game_result
        self.player_1id = player_1id
        self.player_2id = player_2id
        self.winner = winner
        self.outcome = outcome 
        self.score = score 

        # The winner gets printed out 
        if self.winner != "":
            print(f"{self.winner} has won the game!")

    
    def sum_logic(self, team_name: str) -> int:
        '''checks the length of the team names = strings, it is used for a 
        "fake" scoring system for the def play_round'''
        return len(team_name)
        

    def brackets_of_tournament(self, id : int = 0 , tournamentid : int = 0, type: str= "", totalItems: int = 0, totalRounds: int = 0, status: str = ""): 
        '''Brackets format of the tournament
        16 to 8 to 4 to 2 to 1 (winner!)'''
        self.id = id
        self.tournamentid = tournamentid
        self.type = type
        self.totalItems = totalItems
        self.totalrounds = totalRounds
        self.status = status 

        # store all matches in a empty list 
        self.matches =  [] # all matches are stored 
        self.rounds = {} # all rounds are stored 
        
        # brackets , round of 16, quartefinals, semifinals , final 
        if self.teams != 16 : 
            raise ValueError ("There has to be at least 16 teams in the Tournament!")
        
        # split 16 teams into two sides (8 teams on the left, 8 teams on the right)        #!!! can be more than 16 teams 
        left_teams = self.teams[:8]
        right_teams = self.teams[8:]

        # rounds of the left teams
        round1_winners_left = self.play_round(left_teams) 
        round2_winners_left = self.play_round(round1_winners_left)
        round3_winners_left = self.play_round(round2_winners_left)
        champion_left = round3_winners_left[0]
        print(f"The winner from the left side is , {champion_left} !")

        # rounds of the right teams
        round1_winners_right = self.play_round(right_teams)
        round2_winners_right = self.play_round (round1_winners_right)
        round3_winners_right = self.play_round (round2_winners_right)
        champion_right= round3_winners_right
        print(f"The winner from the right side is , {champion_right}")


    def play_round(self, teams: list[str]) ->list [str]:
        winners = list[str] = []

        for  i in range (0, len(teams), 2):
             team1= teams[i]
             team2 = [i + 1]

             score1 = self.sum_logic(team1)
             score2 = self.sum_logic(team2)

             if score1 >= score2:
                winners.append(team1)

             else: 
                winners.append(team2)
        
        return winners 
    
        # Úrslitaleikur / FINAL
        finalists = self.play_round([champion_left, champion_right])
    
        final_winner = finalists[0]
        print(f"The Tournamenyt winner is , {final_winner} !")

# þarf að vera svo Organizer virki rétt!!
    # def new_tourney(self, tournament_obj: Tournament) -> list:
    #     '''want to return as a list, not a dict to have it easier to read'''
    #     tournament_list = [
    #         tournament_obj.unique_name,
    #         tournament_obj.start_date.strftime("%d/%m/%Y"),
    #         tournament_obj.end_date.strftime("%d/%m/%Y"),
    #         tournament_obj.venue,
    #         tournament_obj.contact_person,
    #         tournament_obj.contact_email,
    #         tournament_obj.contact_phone
    #     ]

    #     return self.tournamentio.create_new_tournament(tournament_list)
    
    # def get_allTournamnets(self):
    #     return self.data.get_all_tournaments()



    
