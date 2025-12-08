from logic_layer.LLTeams import LLTeams
from data_layer.PlayerIO import PlayerIO


def main():
    ll_teams = LLTeams()

    # 1 Print all teams
    print("=== Teams loaded ===")
    for t in ll_teams.view_teams():
        print(f"- {t.name} (captain: {t.captain})")

    # 2 Print all players before
    print("\n=== Players before ===")
    players_before = PlayerIO.get_players()
    for p in players_before:
        print(f"{p.name} -> {p.team} (points: {p.points})")


    # 3 Try moving player to another team
    team_name = "Fantom"
    player_name = "Oppenhim"   # is now in " TEAM" according to csv

    print(f"\n>>> Moving '{player_name}' to the team: '{team_name}'")
    try:
        added_player = ll_teams.add_player_to_team(team_name, player_name)
        print(f"OK! {added_player.name} is now in {added_player.team}")
    except ValueError as e:
        print("Error in add_player_to_team:", e)

    # 4 Print all players after change
    print("\n=== Players after ===")
    players_after = PlayerIO.get_players()
    for p in players_after:
        print(f"{p.name} -> {p.team} (points: {p.points})")



if __name__ == "__main__":
    main()