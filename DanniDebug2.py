from logic_layer.LL_api import LL_API


def getplayer():
    players = LL_API.getplayers()
    return players

getplayer()
