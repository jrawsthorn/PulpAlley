from League import *


class Pulp:
    def __init__(self):
        self.__all_my_leagues = []

    def add_league(self, name):
        league = League(name)
        self.__all_my_leagues.append(league)
        return league

    def find_league(self, name):
        league = None
        for league in self.__all_my_leagues:
            if name == league.get_name():
                break
        return league
