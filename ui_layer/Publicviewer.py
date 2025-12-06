from logic_layer.LL_api import LL_API

class PublicViewer:
    
    userinput = int(input("Veldu ID leikmanns milli 1-57: "))
    def getplayerPublic():
        api = LL_API()        
        players = api.getPlayerPublic()
        return players

    player_dict = getplayerPublic()
    print(player_dict[userinput])

    userinputTeams = int(input("Veldu númer liðs 1-18: "))        
    def getTeamPublic():
        api = LL_API()
        teams = api.getTeamPublic()
        return teams

    teams, captain = getTeamPublic()
    print(f"Team: {teams[userinputTeams]}, Captain: {captain[userinputTeams]}")