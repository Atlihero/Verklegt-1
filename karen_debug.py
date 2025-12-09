#klúbbur
# = unique name
# have its own colors
# have country and hometown

#be able to keep the point for each club, be able to see who won each game both team and club
#should be able to find a player and what club he has played for

# for each club
    # what team has the most point 
    # what team has most wins
    # what team has the most in earnings
    # what team has competed in the most games


from ui_layer.OrganizerUI import OrganizerUI

def main():
    ui = OrganizerUI()

    print("--- Create Player ---")
    player = ui.get_player_info()
    print(player)

    print("\n--- Create Tournament ---")
    tournament = ui.createTournament()
    print(tournament)

if __name__ == "__main__":
    main()
