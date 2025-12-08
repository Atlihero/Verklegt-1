from logic_layer.LLTournament import Tournament

def main():
    # create a tournament instance
    t = Tournament("Debug Tournament")

    # call one method just to see it works
    result = t.sum_logic("Team1")
    print("sum_logic('Team1') returned:", result)

if __name__ == "__main__":
    main()