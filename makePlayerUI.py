from logic_layer.LLPlayers import LLPlayer #þetta þarf að vera wrapper == API !!!!

def get_player_info():
    
    name = input("Enter full name of player: ")

    while True:
        dob_str = input("Enter player date of birth (DD/MM/YYYY): ")
        try:
            dob = LLPlayer.validate_dob(dob_str)
            break
        except ValueError as error:
            print(error)
            
    address = input("Enter player's home address: ")
    
    while True:
        phone_number = input("Enter player's phone number: ")
        try:
            LLPlayer.validate_phone(phone_number)
            break
        except ValueError as error:
            print(error)

    while True:
        player_email = input("Enter the player's email address: ")
        try: 
            LLPlayer.validate_email(player_email)
            break
        except ValueError as error:
            print(error)
    
    while True:
        handle = input("Enter player's handle: ")
        try:  
            handle = LLPlayer.validate_handle(handle)
            break
        except ValueError as error:
            print(error)

    while True:
        link = input("Enter a link (press 'Enter' to skip): ")
        try:
            link = LLPlayer.validate_link(link)
            break
        except ValueError as error:
            print(error)

    player = LLPlayer.create_player(name, dob, address, phone_number, player_email, handle, link)
    print("Player created successfully!")
    return player
