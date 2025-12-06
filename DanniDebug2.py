from logic_layer.LL_api import LL_API

while True:
    print("\nValmynd:")
    print("1. Get players")
    print("2. Get team")

    val = input("Veldu verkefni (1-2): ")

    if val == "1":
        userinput = int(input("Veldu ID leikmanns milli 1-57: "))
        class PublicViewer:     
            def getplayerPublic():
                api = LL_API()        
                players = api.getPlayerPublic()
                return players
                
            player, team = getplayerPublic()
            print(f"Player: {player[userinput]}, Team: {team[userinput]}")

    if val == "2":
        userinputTeams = int(input("Veldu númer liðs 1-18: "))
        class PublicViewer:

            def getTeamPublic():
                api = LL_API()
                teams = api.getTeamPublic()
                return teams

            teams, captain = getTeamPublic()
            print(f"Team: {teams[userinputTeams]}, Captain: {captain[userinputTeams]}")