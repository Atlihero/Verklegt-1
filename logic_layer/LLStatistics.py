import csv
from typing import Dict, Any, List      #skoða seinna
from logic_layer.LLTeams import LLTeams
from data_layer.TeamIO import TEAM_PATH
from data_layer.PlayerIO import PlayerIO
from data_layer.TeamIO import TeamIO

class LLStatistics:
    def __init__(self):
        self.ll_teams = LLTeams()


    def calculate_team_stats(self, team_name: str) -> Dict[str, Any]:
        """Points after winning tournament,
        what tournaments he has particapated in"""

        # Validate that team exists in LLTeams
        team = self.ll_teams.get_team_by_name(team_name)
        if team is None:
            raise ValueError("A Team with this name does not exist in LLTeam")
        
        # Get wins and points from TeamIO
        wins, points = TeamIO.get_team_wins_points(team_name)

        # Get all players and filter the ones in this team
        players = PlayerIO.get_players()
        players_in_team = [p for p in players if p.team == team_name]

        # Find player with most points
        top_scorer = None
        if players_in_team:
            top_scorer = max(players_in_team, key=lambda p: p.points)

        tournaments_won = 0
        player_most_wins = None

        return {
            "team": team,
            "wins": wins,
            "points": points,
            "top_scorer": top_scorer,
            "tournaments_won": tournaments_won,
            "player_most_wins": player_most_wins

        }



    def calculate_player_stats(self, player_name: str) -> Dict[str, Any]:
        """ What team does he play for, what club"""
        
        # Get all players
        players = PlayerIO.get_players()

        # Find Player
        player = None
        for p in players:
            if p.name == player_name:
                player = p
                break
        
        if player is None:
            raise ValueError("Player with this name was not found")
        
        # Find players points 
        raw_points = getattr(player, "points", 0)
        try:
            points = int(raw_points)
        except (ValueError, TypeError):
            points = 0

        # Find players team
        team_name = getattr(player, "team", "")


        #PLACE HOLDER FOR LATER 
        games_won = 0
        club_name = None
        tournaments = []

        return {
            "player": player,
            "team": team_name,
            "points": points,
            "games_won": games_won,
            "club": club_name,
            "tournaments": tournaments,
        }


    def calculate_club_stats() -> Dict[str, Any]:
        """Glubs poinst and wins
        has a country and hometown"""
        pass


    def view_results():
        "viewer wants to view final results"
        pass



