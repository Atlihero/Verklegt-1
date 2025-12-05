class OrganizerUI:
    def __init__(self):
        h = 1
    
    def get_player(self):
        players = LL_API.getplayers()
        return players

    def get_playerStats(self):
        player_stats = LL_API.getPlayer_stats()
        return player_stats
    
    def valid_date_of_birth(self, dob):
        is_valid_DOB = LL_API.valid_dob(dob)
        return is_valid_DOB
    
    def valid_phonenumber(self, phone):
        is_valid_phone = LL_API.valid_phone(phone)
        return is_valid_phone
    
    def validEmail(self, email):
        is_validEmail = LL_API.valid_email(email)
        return is_validEmail
    
    def validHandle(self, handle):
        is_validHandle = LL_API.valid_handle(handle)
        return is_validHandle
    
    def valid_link(self, link):
        is_valid_link = LL_API.validate_link(link)
        return is_valid_link
    
    def createPlayer(self, name, dob_string, phone, email, handle, link):
        createsPlayer = LL_API.create_player(name, dob_string, phone, email, handle, link)
        return createsPlayer

    def get_team(self):
        team = LL_API.get_teams()
        return team