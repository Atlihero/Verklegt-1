from logic_layer.LL_api import LL_API

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Get team")
    print("3. Create tournament")
    print("Q. Quit")

    val = input("Veldu verkefni (1-3): ")

    if val == "1":
        userinput = int(input("Veldu ID leikmanns milli 1-57: "))
        api = LL_API()
        players, teams = api.getPlayerpublic()
        print(f"Player: {players[userinput]}, Team: {teams[userinput]}")

    elif val == "2":
        userinputTeams = int(input("Veldu númer liðs 1-18: "))
        api = LL_API()
        teams, captains = api.getTeamPublic()
        print(f"Team: {teams[userinputTeams]}, Captain: {captains[userinputTeams]}")

    elif val == "3":
        unique_name = input("Create a unique name for the tournament: ")
        start_date = input("Select the start date of the tournament: ")
        end_date = input("Select end date for the tournament: ")
        venue = input("Select the venue for the tournament: ")
        contact_person = input("Name the contact person for this tournament: ")
        contact_email = input("What is the contact email for this tournament: ")
        contact_phone = input("What is the contact phone for this tournament: ")

        tournament_dict = {
            "unique_name": unique_name,
            "start_date": start_date,
            "end_date": end_date,
            "venue": venue,
            "contact_person": contact_person,
            "contact_email": contact_email,
            "contact_phone": contact_phone
        }

        api = LL_API()
        result = api.create_new_tournaments(tournament_dict)
        print(result) 

    elif val.upper() == "Q":
        print("You have quit the program")
        break
