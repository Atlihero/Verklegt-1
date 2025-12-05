# test_LLStatistics.py

from logic_layer.LLStatistics import LLStatistics

def main():
    stats_ll = LLStatistics()

    # === TEAM STATS TEST ===
    team_name = "Fantom"

    try:
        team_stats = stats_ll.calculate_team_stats(team_name)
    except ValueError as e:
        print("Villa í team stats:", e)
        return

    team = team_stats["team"]
    print(f"=== Tölfræði fyrir lið: {team.name} ===")
    print(f"- Fyrirliði: {team.captain}")
    print(f"- Wins (leikir unnir): {team_stats['wins']}")
    print(f"- Points (stig liðs): {team_stats['points']}")

    top = team_stats["top_scorer"]
    if top is not None:
        print(f"- Top scorer í liðinu: {top.name} ({top.points} stig)")
    else:
        print("- Enginn leikmaður fannst í þessu liði")

    print(f"- Mót unnin (placeholder): {team_stats['tournaments_won']}")
    print(f"- Leikmaður með flesta sigra (placeholder): {team_stats['player_most_wins']}")

    # === PLAYER STATS TEST ===
    print("\n=== Player stats test ===")
    player_name = "Oppenhim"   # veldu einhvern sem þú veist að er til í CSV

    try:
        p_stats = stats_ll.calculate_player_stats(player_name)
    except ValueError as e:
        print("Villa í player stats:", e)
        return

    p = p_stats["player"]
    print(f"Leikmaður: {p.name}")
    print(f"- Lið: {p_stats['team']}")
    print(f"- Stig alls: {p_stats['points']}")
    print(f"- Sigrar í leikjum (placeholder): {p_stats['games_won']}")
    print(f"- Klúbbur (placeholder): {p_stats['club']}")
    print(f"- Mót sem hann hefur tekið þátt í (placeholder): {p_stats['tournaments']}")

if __name__ == "__main__":
    main()
