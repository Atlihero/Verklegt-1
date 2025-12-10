from data_layer.data_api import DataAPI

data = DataAPI()
players = data.get_all_players()

for p in players[:5]:
    print(p.name, "| team:", p.team)
