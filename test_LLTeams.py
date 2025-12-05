from logic_layer.LLTeams import LLTeams
from data_layer.PlayerIO import PlayerIO


def main():
    ll_teams = LLTeams()

    # 1. Prenta öll lið
    print("=== Lið sem voru loaduð ===")
    for t in ll_teams.view_teams():
        print(f"- {t.name} (captain: {t.captain})")

    # 2. Prenta alla leikmenn ÁÐUR
    print("\n=== Leikmenn ÁÐUR ===")
    players_before = PlayerIO.get_players()
    for p in players_before:
        print(f"{p.name} -> {p.team} (points: {p.points})")


    # 3. Prófa að færa leikmann í annað lið
    team_name = "Fantom"
    player_name = "Oppenhim"   # er núna í "Black in Yellow" samkvæmt CSV

    print(f"\n>>> Bæti '{player_name}' í liðið '{team_name}'")
    try:
        # ATH: LLTeams.add_player_to_team þarf að taka (team_name, player_name)
        added_player = ll_teams.add_player_to_team(team_name, player_name)
        print(f"OK! {added_player.name} er núna í {added_player.team}")
    except ValueError as e:
        print("Villa í add_player_to_team:", e)

    # 4. Prenta alla leikmenn EFTIR
    print("\n=== Leikmenn EFTIR ===")
    players_after = PlayerIO.get_players()
    for p in players_after:
        print(f"{p.name} -> {p.team} (points: {p.points})")



if __name__ == "__main__":
    main()