# test_LLStatistics.py

from logic_layer.LLStatistics import LLStatistics

def main():
    stats_ll = LLStatistics()

    # === TEAM STATS TEST ===
    team_name = "Black in Yellow"

    try:
        team_stats = stats_ll.calculate_team_stats(team_name)
    except ValueError as e:
        print("Error in team stats:", e)
        return

    team = team_stats["team"]
    print(f"=== Statistics for team: {team.name} ===")
    print(f"- Captain: {team.captain}")
    print(f"- Wins: {team_stats['wins']}")
    print(f"- Points: {team_stats['points']}")

    top = team_stats["top_scorer"]
    if top is not None:
        print(f"- Top scorer in the team: {top.name} ({top.points} points)")
    else:
        print("- No player found in this team")

    print(f"- Tournaments won: {team_stats['tournaments_won']}")
    print(f"- Player with most wins: {team_stats['player_most_wins']}")

    # === PLAYER STATS TEST ===
    print("\n=== Player stats test ===")
    player_name = "Bruse wayne"   # veldu einhvern sem þú veist að er til í CSV

    try:
        p_stats = stats_ll.calculate_player_stats(player_name)
    except ValueError as e:
        print("Error in player stats:", e)
        return

    p = p_stats["player"]
    print(f"Player: {p.name}")
    print(f"- Team: {p_stats['team']}")
    print(f"- Points: {p_stats['points']}")
    print(f"- Games won: {p_stats['games_won']}")
    print(f"- Club: {p_stats['club']}")
    print(f"- Tournaments he has particapated in: {p_stats['tournaments']}")

if __name__ == "__main__":
    main()
