from Character import *


class Leader(Character):
    def __init__(self, name,
                 health_die_num, health_die_type,
                 brawl_die_num, brawl_die_type,
                 shoot_die_num, shoot_die_type,
                 dodge_die_num, dodge_die_type,
                 might_die_num, might_die_type,
                 finesse_die_num, finesse_die_type,
                 cunning_die_num, cunning_die_type):

        char_type = "Leader"
        level = 4
        ability_num = 3
        slots = 0

        Character.__init__(self, char_type, level, ability_num, slots, name,
                           health_die_num, health_die_type,
                           brawl_die_num, brawl_die_type,
                           shoot_die_num, shoot_die_type,
                           dodge_die_num, dodge_die_type,
                           might_die_num, might_die_type,
                           finesse_die_num, finesse_die_type,
                           cunning_die_num, cunning_die_type)
