from logic_layer.LL_api import LL_API

class Orginizer:
    def create_player(self):
        self.cr_player = LL_API.create_player()
        return self.cr_player

    def create_tournament(self):
        self.cr_tournament = LL_API#vantar.tournament
        return self.cr_tournament

    def create_team(self):
        self.cr_team = LL_API#vantar .create_team
        return self.cr_team

    def make_captain(self):
        self.mk_captain = LL_API#vantar create captein
        return self.mk_captain