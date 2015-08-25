from Ability import *
from MyException import *


class AbilityFactory:
    def __init__(self):
        self.__all_my_abilities = []

    def find_ability(self, ability_name):
        an_ability = None
        for ability in self.__all_my_abilities:
            if ability_name == ability.get_name():
                an_ability = ability
                break
        return an_ability

    def has_ability(self, ability_name):
        result = False
        for ability in self.__all_my_abilities:
            if ability_name == ability.get_name():
                result = True
                break
        return result

    def load_abilities(self):
        try:
            with open('abilities.txt', "r") as file:
                for line in file:
                    ability_data = line.split("|")
                    ability = Ability(ability_data[0], ability_data[1],
                                      ability_data[2].rstrip("\n"))
                    self.__all_my_abilities.append(ability)
        except IOError:
            raise MyException("Cannot find abilities file. No character will "
                              "be created.\nEnsure the file 'abilities.txt'"
                              "sits within the local directory of this "
                              "application.")
