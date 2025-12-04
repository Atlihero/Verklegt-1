# from datetime import datetime

# def player_info():
#     date_input=(input("Enter a date (DD/MM/YYYY): "))

#     try:
#         entered_date = datetime.strptime(date_input, "%d/%m/%Y")

#         if entered_date > datetime.now():
#             print("The date cannot be in the future.")
#             return player_info()

#         else:
#             day = entered_date.day
#             month = entered_date.month
#             year = entered_date.year

#             return f'{day}/{month}/{year}'
    
#     except ValueError:
#         print("Invalid date. Use DD/MM/YYYY.")
#         return player_info()


# date_input = player_info()

# print(date_input)



# def player_phone():
#     phone_number = input("Enter player's phone number: ")
#     try:
        
                        
#     except ValueError:
#         print("Invalid phone number. Try again.")

def add_to_team(self):
        ll = LLTeams()
        
        # find existing players
        members = self.get_team_members()
        if len(members) >= self.MAX_TEAM_MEMBERS:
            raise ValueError("There are already 5 players in your team.")
       
        # Input fyrir nafn
        # kalla í fallið add_player frá LLTeams klasa
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni - Team is full
        # villa ef reynt er að bæta við manni sem er nú þegar í liði
        pass



def remove_from_team(self):
    remove_player = input("Please enter the name of the player you want to remove: ")
    # input fyrir nafn sem á að eyða úr liðslista
    # warning signs 'u sure u want to delete this person?'
    # villa ef reynt er að taka út leikmann sem er ekki í liðinu

    
