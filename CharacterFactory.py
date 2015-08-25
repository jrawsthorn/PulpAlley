from Leader import *
from Sidekick import *
from Ally import *
from Follower import *


class CharacterFactory:
    @staticmethod
    def create_character(char_type, name,
                         health_die_num, health_die_type,
                         brawl_die_num, brawl_die_type,
                         shoot_die_num, shoot_die_type,
                         dodge_die_num, dodge_die_type,
                         might_die_num, might_die_type,
                         finesse_die_num, finesse_die_type,
                         cunning_die_num, cunning_die_type):

        if char_type == "Leader":
            character = Leader(name, health_die_num, health_die_type,
                               brawl_die_num, brawl_die_type,
                               shoot_die_num, shoot_die_type,
                               dodge_die_num, dodge_die_type,
                               might_die_num, might_die_type,
                               finesse_die_num, finesse_die_type,
                               cunning_die_num, cunning_die_type)
            return character
        elif char_type == "Sidekick":
            character = Sidekick(name, health_die_num, health_die_type,
                                 brawl_die_num, brawl_die_type,
                                 shoot_die_num, shoot_die_type,
                                 dodge_die_num, dodge_die_type,
                                 might_die_num, might_die_type,
                                 finesse_die_num, finesse_die_type,
                                 cunning_die_num, cunning_die_type)
            return character
        elif char_type == "Ally":
            character = Ally(name, health_die_num, health_die_type,
                             brawl_die_num, brawl_die_type,
                             shoot_die_num, shoot_die_type,
                             dodge_die_num, dodge_die_type,
                             might_die_num, might_die_type,
                             finesse_die_num, finesse_die_type,
                             cunning_die_num, cunning_die_type)
            return character
        elif char_type == "Follower":
            character = Follower(name, health_die_num, health_die_type,
                                 brawl_die_num, brawl_die_type,
                                 shoot_die_num, shoot_die_type,
                                 dodge_die_num, dodge_die_type,
                                 might_die_num, might_die_type,
                                 finesse_die_num, finesse_die_type,
                                 cunning_die_num, cunning_die_type)
            return character
