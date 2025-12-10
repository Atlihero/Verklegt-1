from logic_layer.LL_api import LL_API

api = LL_API()
teams = api.view_teams()
print("Loaded teams:", teams)
for t in teams:
    print("Team:", t.name, "| Captain:", t.captain)
