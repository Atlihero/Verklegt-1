import csv

TEAM_PATH: str = r"_data\Teams.csv"

class TeamIO:

    def get_team():
        Teams = []
        with open(TEAM_PATH, "r", encoding="utf-8") as csvfile:
            reader  = csvfile.readlines()
            for row in reader:
                Teams.append(row)
        return Teams

    def add_new_team():
        "bætir við liði sem user býr til"
        pass

    def get_team_stats():
        "Sækir tölfræði liða"
        pass
