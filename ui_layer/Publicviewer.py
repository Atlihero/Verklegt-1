from logic_layer.LL_api import LL_API
api = LL_API()
class PublicViewer:

    def getplayerPublic():      
        players = api.get_playerPublic()
        return players
    
    def getTeamsPublic():
        teams = api.get_teams_public()
        return teams
    
    def view_schedule(games, title="Current Games"):
        print(f"\n=== {title} ===")
        for g in games:
            print(f"{g['match_number']:>2}: {g['round']} | {g['team_a']} vs {g['team_b']} | "
                f"Score: {g['score_a'] or '-'}-{g['score_b'] or '-'} | Winner: {g['winner'] or '-'}")
            return games

        tournament_name = input("Enter tournament name: ").strip()
        games = api.get_game_by_tournamentName(tournament_name)

