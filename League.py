from CharacterFactory import *
from prettyTable import PrettyTable
from MyException import *


class League:

    def __init__(self, name):
        self.__name = name
        self.__my_character_factory = CharacterFactory()
        self.__all_my_characters = []

    def get_name(self):
        return self.__name

    def add_character(self, char_type, name,
                      health_die_num, health_die_type,
                      brawl_die_num, brawl_die_type,
                      shoot_die_num, shoot_die_type,
                      dodge_die_num, dodge_die_type,
                      might_die_num, might_die_type,
                      finesse_die_num, finesse_die_type,
                      cunning_die_num, cunning_die_type):

        character = self.__my_character_factory.create_character(
            char_type, name,
            health_die_num, health_die_type,
            brawl_die_num, brawl_die_type,
            shoot_die_num, shoot_die_type,
            dodge_die_num, dodge_die_type,
            might_die_num, might_die_type,
            finesse_die_num, finesse_die_type,
            cunning_die_num, cunning_die_type)

        self.__all_my_characters.append(character)
        return character

    def find_character(self, name):
        a_character = None
        for character in self.__all_my_characters:
            if name == character.get_name():
                a_character = character
                break
        return a_character

    def display(self):
        print("\n\n\n\nLeague - " + self.get_name())
        for character in self.__all_my_characters:
            print(character.display_skills())
            print(character.display_abilities())
            print("\n")

    def display_unit_test(self):
        result = self.get_name()
        for character in self.__all_my_characters:
            result += "\n    " + character.display_unit_test()

        return result

    def is_roster_full(self):
        slots = 0
        for character in self.__all_my_characters:
            slots += character.get_slots()

        if slots < 10:
            result = False
        else:
            result = True

        return result

    def has_leader(self):
        result = False
        for character in self.__all_my_characters:
            if character.get_type() == "Leader":
                result = True
                break
        return result

    def has_sidekick(self):
        result = False
        for character in self.__all_my_characters:
            if character.get_type() == "Sidekick":
                result = True
                break

        return result

    def count_characters(self, char_type):
        i = 0
        for character in self.__all_my_characters:
            if char_type == character.get_type():
                i += 1
        return i

    def get_all_my_characters(self):
        return self.__all_my_characters
