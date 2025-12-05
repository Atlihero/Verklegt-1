class Tournament():
    def __init__(self, name : str ):

        self.tournament = name
        self._next_game_id  = 1 


        self.teams = [ "Team1" , "Team2", "Team3 ", "Team4", "Team5", "Team6", "Team7", "Team8", 
                    "Team9", "Team10", "Team11", "Team12", "Team13", "Team14", "Team15", "Team16"]

# CONTACT Information very Important , Also Updated 


    def get_contact_info(self, contact:str = "", email:str="", phone : str = ""):
        
        self.contact = contact 
        self.email = email 
        self.phone = phone 

    def update_contact_info(self, new_contact: str= "", new_email: str= "", new_phone : str = ""):

        if new_contact:
            self.new_contact = new_contact
        if new_email:
            self.new_email = new_email
        if new_phone:
            self.new_phone = new_phone

    def register_team(self, team_name: str= "", players : list[str]= None):
        
        if self.find.team.by_name(team_name) is not None:
            raise ValueError(f"The team {team_name} already exists ")
        
        self.team_name = team_name



        if len(players) < 1: 
            raise ValueError ("A team must have at least 1 player ")
        
        # new team object , not a paramater yk 
        team = team(name=team_name , players = players )
        
        self.tournament.teams.append(team)

        return team 


    def schedule_games(self, start_date : str = "", end_date : str =  "", teams : list = 0, venue : str = ""):
        
        self.start_date = start_date 
        self.end_date = end_date 
        self.venue = venue 
        self.teams = teams 

    # store all matches in a empty list 

        self.matches =  []     # where all the matches are being stored 
        self.rounds = {}       # where all the rounds are being stored 



        # requirements to schedule a game  
        if len(teams) < 2 : 
            raise ValueError ("For a match there have to be at least 2 Teams")
        
        if not start_date:
            raise ValueError ("There is no start date given")
        
        if not end_date: 
            raise ValueError("There is no End Date given")
        
        if not venue : 
            raise ValueError("There is no Venue to be played in")
        


    def record_result(self, game_result : int = 0, player_1id : str = "", player_2id : str = "", winner : str = "", outcome : str = "", score : str=  ""):


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
        
        
        return len(team_name)


    #brackets format of the tournament
    # 16 to 8 to 4 to 2 to 1 (winner!)

    def brackets_of_tournament(self, id : int = 0 , tournamentid : int = 0, type: str= "", totalItems: int = 0, totalRounds: int = 0, status: str = ""): 

        self.id = id
        self.tournamentid = tournamentid
        self.type = type
        self.totalItems = totalItems
        self.totalrounds = totalRounds
        self.status = status 


# store all matches in a empty list 

        self.matches =  []     # where all the matches are being stored 
        self.rounds = {}       # where all the rounds are being stored 



# brackets , round of 16, quartefinals, semifinals , final 

        if self.teams != 16 : 
            raise ValueError ("There has to be at least 16 teams in the Tournament!")
        

    # splitting the tournament scheme into a left and right side

        left_teams = [ "team1", "team2", "team3" , "team4"
                      "team5", "team6" , "team7" ,"team8"]
        

        right_teams = ["team9" ,"team10" ,"team11" ,"team12", 
                       "team13" ,"team14", "team15", "team16"]
    
           
        
    def play_round(self, teams: list[str]) ->list [str]:
        winners = list[str] = []

        # example this goes through the left teams , from 0 to 7 , in total 8 "left" teams

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
    

    # implement left teams_list (team1 to team8)


    left_teams = [ "team1", "team2", "team3" , "team4",
                 "team5", "team6" , "team7" ,"team8"]
    # left side 

    # 8 teams play and 4 teams advance
    round1_winners_left = play_round(left_teams) 

    # 4 teams play and 2 teams advance
    round2_winners_left = play_round(round1_winners_left)


    # 2 teams play and 1 teams addvcanc etc 
    round3_winners_left = play_round(round2_winners_left)

    champion_left = round3_winners_left[0]

    print(f"The winner from the left side is , {champion_left} !")



    right_teams = [ "team9" ,"team10" ,"team11" ,"team12", 
                  "team13" ,"team14", "team15", "team16"]

    # right side 


    round1_winners_right = play_round(right_teams)
    
    round2_winners_right = play_round (round1_winners_right)

    round3_winners_right = play_round (round2_winners_right)

    champion_right= round3_winners_right


    print(f"The winner from the right side is , {champion_right}")


    # Úrslitaleikur / FINAL

    finalists = play_round([champion_left, champion_right])

    final_winner = finalists[0]
    final_winner= print(f"The Tournamenyt winner is , {final_winner} !")



    


        

    










