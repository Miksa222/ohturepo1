from player import Player
from player_reader import PlayerReader
from statistics_service import StatisticsService
import unittest



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats=StatisticsService(PlayerReaderStub())

    def test_search_player_found(self):
        name="Kurri"
        self.assertEqual(self.stats.search("Kurri").name,name)

    def test_search_player_wrongname(self):
        self.assertEqual(self.stats.search("Nobody"),None)

    def test_team_player_amount_correct(self):
        self.assertEqual(len(self.stats.team("EDM")),3)

    def test_sort_by_points_correct(self):
        self.assertEqual(self.stats.search("Kurri").points,90)

    def test_top_correct_order(self):
        top_list=self.stats.top(4)
        top_list_names=[]
        for i in top_list :
            top_list_names.append(i.name)

        self.assertEqual(top_list_names,["Gretzky","Lemieux","Yzerman","Kurri"])



