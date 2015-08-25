from AbilityFactory import *
from prettyTable import PrettyTable


class Character:
    def __init__(self, char_type, level, ability_num, slots, name,
                 health_die_num, health_die_type,
                 brawl_die_num, brawl_die_type,
                 shoot_die_num, shoot_die_type,
                 dodge_die_num, dodge_die_type,
                 might_die_num, might_die_type,
                 finesse_die_num, finesse_die_type,
                 cunning_die_num, cunning_die_type):

        self._type = char_type
        self._level = level
        self._name = name
        self._ability_num = ability_num
        self._slots = slots
        self._health_die_num = health_die_num
        self._health_die_type = health_die_type
        self._brawl_die_num = brawl_die_num
        self._brawl_die_type = brawl_die_type
        self._shoot_die_num = shoot_die_num
        self._shoot_die_type = shoot_die_type
        self._dodge_die_num = dodge_die_num
        self._dodge_die_type = dodge_die_type
        self._might_die_num = might_die_num
        self._might_die_type = might_die_type
        self._finesse_die_num = finesse_die_num
        self._finesse_die_type = finesse_die_type
        self._cunning_die_num = cunning_die_num
        self._cunning_die_type = cunning_die_type
        self._my_ability_factory = AbilityFactory()
        self._all_my_abilities = []

        self._my_ability_factory.load_abilities()

    def modify_skills(self, ability):
        description = ability.get_description()

        if '+1 die' in description:
            if 'Health' in description:
                self.increase_health_die_num()
            elif 'Brawl' in description:
                self.increase_brawl_die_num()
            elif 'Shoot' in description:
                self.increase_shoot_die_num()
            elif 'Dodge' in description:
                self.increase_dodge_die_num()
            elif 'Might' in description:
                self.increase_might_die_num()
            elif 'Finesse' in description:
                self.increase_finesse_die_num()
            elif 'Cunning' in description:
                self.increase_cunning_die_num()

            ability.set_description(description + "(included above)")

    def add_ability(self, ability_name):
        ability = self._my_ability_factory.find_ability(ability_name)
        if ((ability.get_level() <= self._level) and
                (self.count_abilities() < self._ability_num)):
            self._all_my_abilities.append(ability)
            self.modify_skills(ability)

    def count_abilities(self):
        return len(self._all_my_abilities)

    def find_ability_index(self, ability_name):
        index = 0
        for ability in self._all_my_abilities:
            if ability_name == ability.get_name():
                break
            index += 1
        return index

    def delete_ability(self, ability_name):
        ability = self.find_ability_index(ability_name)
        del self._all_my_abilities[ability]

    def get_type(self):
        return self._type

    def get_level(self):
        return self._level

    def get_name(self):
        return self._name

    def get_slots(self):
        return self._slots

    def get_health_die_num(self):
        return self._health_die_num

    def get_health_die_type(self):
        return self._health_die_type

    def increase_health_die_num(self):
        self._health_die_num += 1

    def get_brawl_die_num(self):
        return self._brawl_die_num

    def get_brawl_die_type(self):
        return self._brawl_die_type

    def increase_brawl_die_num(self):
        self._brawl_die_num += 1

    def get_shoot_die_num(self):
        return self._shoot_die_num

    def get_shoot_die_type(self):
        return self._shoot_die_type

    def increase_shoot_die_num(self):
        self._shoot_die_num += 1

    def get_dodge_die_num(self):
        return self._dodge_die_num

    def get_dodge_die_type(self):
        return self._dodge_die_type

    def increase_dodge_die_num(self):
        self._dodge_die_num += 1

    def get_might_die_num(self):
        return self._might_die_num

    def get_might_die_type(self):
        return self._might_die_type

    def increase_might_die_num(self):
        self._might_die_num += 1

    def get_finesse_die_num(self):
        return self._finesse_die_num

    def get_finesse_die_type(self):
        return self._finesse_die_type

    def increase_finesse_die_num(self):
        self._finesse_die_num += 1

    def get_cunning_die_num(self):
        return self._cunning_die_num

    def get_cunning_die_type(self):
        return self._cunning_die_type

    def increase_cunning_die_num(self):
        self._cunning_die_num += 1

    @staticmethod
    def concat_skill(die_num, die_type):
        return str(die_num) + "d" + str(die_type)

    def display_skills(self):
        skills_table = PrettyTable(["Type              ", "Name              ",
                                   "Health", "Brawl", "Shoot", "Dodge",
                                    "Might", "Finesse", "Cunning"])
        skills_table.align["Type              "] = "l"
        skills_table.align["Name              "] = "l"

        skills_table.add_row([self._type, self._name,
                             self.concat_skill(self.get_health_die_num(),
                                               self.get_health_die_type()),
                             self.concat_skill(self.get_brawl_die_num(),
                                               self.get_brawl_die_type()),
                             self.concat_skill(self.get_shoot_die_num(),
                                               self.get_shoot_die_type()),
                             self.concat_skill(self.get_dodge_die_num(),
                                               self.get_dodge_die_type()),
                             self.concat_skill(self.get_might_die_num(),
                                               self.get_might_die_type()),
                             self.concat_skill(self.get_finesse_die_num(),
                                               self.get_finesse_die_type()),
                             self.concat_skill(self.get_cunning_die_num(),
                                               self.get_cunning_die_type())])

        return skills_table

    def display_abilities(self):
        abilities_table = PrettyTable(["Ability           ", "Description     "
                                                             "                "
                                                             "                "
                                                             "                "
                                                             "                "
                                                             "                "
                                                             "              "])
        abilities_table.align["Ability           "] = "l"
        abilities_table.align["Description                                    "
                              "                                               "
                              "                "] = "l"

        if self._all_my_abilities:
            for ability in self._all_my_abilities:
                abilities_table.add_row([
                    ability.get_name(), ability.get_description()])
        return abilities_table

    def display_unit_test(self):
        result = (self._type + " " + self._name +
                  " h=" + self.concat_skill(self.get_health_die_num(),
                                            self.get_health_die_type()) +
                  " b=" + self.concat_skill(self.get_brawl_die_num(),
                                            self.get_brawl_die_type()) +
                  " s=" + self.concat_skill(self.get_shoot_die_num(),
                                            self.get_shoot_die_type()) +
                  " d=" + self.concat_skill(self.get_dodge_die_num(),
                                            self.get_dodge_die_type()) +
                  " m=" + self.concat_skill(self.get_might_die_num(),
                                            self.get_might_die_type()) +
                  " f=" + self.concat_skill(self.get_finesse_die_num(),
                                            self.get_finesse_die_type()) +
                  " c=" + self.concat_skill(self.get_cunning_die_num(),
                                            self.get_cunning_die_type()))

        if self._all_my_abilities:
            for ability in self._all_my_abilities:
                result += " +" + ability.display_unit_test()
        return result
