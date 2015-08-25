import re
from AbilityFactory import *
__author__ = 'JRaw'


class InputValidator:
    __base_input = ""
    __char_type = ""
    __char_name = ""
    __skill_list = []
    __ability_list = ""
    __error_msg = ""
    __skill_pattern = re.compile('^[a-z][=][1-9][d][1-9][1-9]?')

    def process_input(self, new_input):
        """
        :param new_input: String from user containing all character information
        :return: returns either the error messages or True

        >>> IV=InputValidator()
        >>> IV.process_input('''Sidekick Arge h=1d10 b=3d8 s=3d8 d=2d6 m=3d8
        ... f=2d6 c=2d6 +Athletic +Fierce''')
        Invalid command/syntax: Incorrect health input, Sidekick must have 'd8'

        >>> IV.process_input('''Ally Enki h=1d10 b=2d6 s=2d6 d=1d6 m=1d6
        ... f=1d6 c=1d6 +Marksman''')
        Invalid command/syntax: Incorrect health input, Ally must have 'd6'

        >>> IV.process_input('''Ally Enki h=d6 b=2d6 s=2d6 d=1d6 m=1d6 f=1d6
        ... c=1d6 +Marksman''')
        Invalid command/syntax: Incorrect health input, should follow example \
syntax: h=1d10 (for Leader)
        """
        if not isinstance(new_input, str):
            return "Invalid command/syntax: Input is not a string"
        elif len(new_input) > 140:
            return "Invalid command/syntax: String is too long to process, " \
                   "max length 140 characters."
        else:
            new_string_list = re.split(' ', new_input.strip())
            try:
                self.has_valid_type(new_string_list[0])
                self.has_valid_name(new_string_list[1])
                self.has_valid_health(new_string_list[2])
                self.has_valid_skills(new_string_list[3:])
                self.has_valid_abilities(new_string_list[9:])
                return self.valid_output(new_string_list)
            except ValueError:
                print("Invalid command/syntax: " + self.__error_msg)
                return None

    def has_valid_type(self, new_character):
        """
        - Checks if the input character type is valid
        - If so then local variable is assigned the type
        - If not then the ValueError is raised
        :param new_character: character section of users input string
        :return: true, or raises exception with unique message

        >>> IV=InputValidator()
        >>> IV.has_valid_type("Leader")
        >>> IV.has_valid_type("Sidekick")
        >>> IV.has_valid_type("Ally")
        >>> IV.has_valid_type("Follower")
        >>> IV.has_valid_type("    Follower    ")

        >>> IV.has_valid_type("Leaderr")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("Leaderr")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("leader")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("leader")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("sidekick")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("ally")
        Traceback (most recent call last):
        ...
        ValueError
        >>> IV.has_valid_type("follower")
        Traceback (most recent call last):
        ...
        ValueError
        """
        char_tup = {"Leader", "Sidekick", "Ally", "Follower"}
        if new_character.strip() in char_tup:
            self.__char_type = new_character
        else:
            self.__error_msg = "Invalid character type, see help"
            raise ValueError

    def has_valid_name(self, new_name):
        """
        - Checks if the length of a character name is valid
        - Could also check for numbers, special characters etc. ???
        :param new_name: name section of the users input string
        :return: True, or ValueError raised

        >>> IV=InputValidator()
        >>> IV.has_valid_name("Singapore-Smith")
        >>> IV.has_valid_name("Singapore-SmithSingapore-Smith")
        Traceback (most recent call last):
        ...
        ValueError
        """
        if len(new_name) <= 16:
            self.__char_name = new_name
        else:
            self.__error_msg = "Name for " + self.__char_type + " is too long"
            raise ValueError

    def has_valid_health(self, new_health):
        """
        - Checks if the health value for the input parameter is valid for
          character type
        :param new_health: Health segment of the users input string
        :return: True, or raises ValueError

        >>> IV=InputValidator()
        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_health("h=1d10")
        >>> IV.set_char_type("Sidekick")
        >>> IV.has_valid_health("h=1d8")

        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_health("h=1d8")
        Traceback (most recent call last):
        ...
        ValueError

        >>> IV.set_char_type("Sidekick")
        >>> IV.has_valid_health("h=1d6")
        Traceback (most recent call last):
        ...
        ValueError
        """
        message = "Incorrect health input, {} must have '{}'"
        if bool(self.__skill_pattern.match(new_health)):
            if self.__char_type == "Leader":
                if new_health.split('d')[1] == '10':
                    self.__skill_list.append(new_health.split('=')[1])
                else:
                    self.__error_msg = message.format("Leader", "d10")
                    raise ValueError
            elif self.__char_type == "Sidekick":
                if new_health.split('d')[1] == '8':
                    self.__skill_list.append(new_health.split('=')[1])
                else:
                    self.__error_msg = message.format("Sidekick", "d8")
                    raise ValueError
            else:
                if new_health.split('d')[1] == '6':
                    self.__skill_list.append(new_health.split('=')[1])
                else:
                    self.__error_msg = message.format(self.__char_type, "d6")
                    raise ValueError
        else:
            self.__error_msg = "Incorrect health input, should follow " \
                               "example syntax: h=1d10 (for Leader)"
            raise ValueError

    def has_valid_skills(self, skill_list):
        """
        - Checks if all the skills in the list contain each type, and in order
        - Runs skill_list through dice number check function
        - Runs skill_list through dice type check function
        :param skill_list: list of six skills excluding health attribute
        :return: True, or raised error with specific error message

        >>> IV=InputValidator()
        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_skills(['b=3d8', 's=3d10', 'd=3d10', 'm=2d8',
        ... 'f=3d10', 'c=2d10'])

        >>> IV.set_char_type("Sidekick")
        >>> IV.has_valid_skills(['b=2d8', 's=3d8', 'd=3d6', 'm=2d8',
        ... 'f=3d6', 'c=2d6'])

        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_skills(['b=2d6', 's=2d6', 'd=1d6', 'm=1d6',
        ... 'f=1d6', 'c=1d6'])
        Traceback (most recent call last):
        ...
        ValueError

        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_skills(['b=3d10', 's=3d10', 'd=3d10', 'm=3d10',
        ... 'f=1d6', 'c=2d6'])
        Traceback (most recent call last):
        ...
        ValueError
        """
        skill_char_list = ['b', 's', 'd', 'm', 'f', 'c']
        for index, item in enumerate(skill_list[:6]):
            if item[0] != skill_char_list[index]:
                self.__error_msg = "Syntax error, skill characters do not " \
                                   "match format: 'b s d m f c' " + item
                raise ValueError
        self.check_dice_count(skill_list[:6])
        self.check_dice_type(str(skill_list[:6]).strip('[]'))

    def has_valid_abilities(self, ability_list):
        """
         - Altered function that checks the abilities are valid
         - Checks whether they are valid for the character type
         - Checks whether the number of abilities is valid for character type
         - Raises a ValueError if any of these fault, with a specific message
        :param ability_list: List of abilities separated from input string
        :return: either true or an error is raised

        >>> IV=InputValidator()

        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_abilities(['+Sharp', '+Deadeye', '+Quick-Shot'])
        >>> IV.set_char_type("Sidekick")
        >>> IV.has_valid_abilities(['+Sharp', '+Deadeye'])
        >>> IV.set_char_type("Ally")
        >>> IV.has_valid_abilities(['+Sharp'])

        >>> IV.set_char_type("Sidekick")
        >>> IV.has_valid_abilities(['+Deadeye', '+Deadeye'])
        Traceback (most recent call last):
        ...
        ValueError

        >>> IV.set_char_type("Leader")
        >>> IV.has_valid_abilities(['+Sharp', '+Deadeye', '+Quick-Shot',
        ... '+Hardened-Veteran'])
        Traceback (most recent call last):
        ...
        ValueError
        """
        abf = AbilityFactory()
        abf.load_abilities()
        ability_count = 0
        previous_abilities = []
        for ability in ability_list:
            ability_count += 1
            if abf.find_ability(ability[1:]):
                new_ab = abf.find_ability(ability[1:])
                if ability[1:] not in previous_abilities:
                    previous_abilities.append(ability[1:])
                else:
                    self.__error_msg = "Ability has already been submitted," \
                                       " only one of each allowed"
                    raise ValueError
                num_error = "Error, too many abilities submitted, max number" \
                            " is {} for {}"
                if self.__char_type == "Leader":
                    if ability_count > 3:
                        self.__error_msg = num_error.format("3", "Leader")
                        raise ValueError
                elif self.__char_type == "Sidekick":
                    if ability_count > 2:
                        self.__error_msg = num_error.format("2", "Sidekick")
                        raise ValueError
                else:
                    if ability_count != 1:
                        self.__error_msg = num_error.format(
                            "1", self.__char_type)
                        raise ValueError
                    if self.__char_type == "Ally":
                        if new_ab.get_level() not in [1, 2]:
                            self.__error_msg = "Ability: '" + ability[1:] + \
                                               "' not valid for " \
                                               "character type 'Ally'"
                            raise ValueError
                    else:
                        if new_ab.get_level() != 1:
                            self.__error_msg = "Ability: '" + ability[1:] + \
                                               "' not valid for character " \
                                               "type 'Follower'"
                            raise ValueError
            else:
                self.__error_msg = "Ability: " + ability[1:] + \
                                   " does not exist"
                raise ValueError

    def check_dice_count(self, skill_list):
        """
        - Checks the dice quantities are valid for corresponding character type
        :param skill_list: list of the skills obtained from process skill_list
        :return: Only on error, else true

        >>> IV=InputValidator()
        >>> IV.set_char_type("Follower")
        >>> IV.check_dice_count(['b=1d10', 's=1d10', 'd=1d10', 'm=1d10',
        ... 'f=1d6', 'c=1d6'])

        >>> IV.set_char_type("Leader")
        >>> IV.check_dice_count(['b=1d10', 's=3d10', 'd=3d10', 'm=3d10',
        ... 'f=2d6', 'c=2d6'])
        Traceback (most recent call last):
        ...
        ValueError
        """
        if self.__char_type == "Leader":
            if self.type_count(skill_list, '3', '2') != [4, 2]:
                self.__error_msg = "Incorrect number of dice, Leader " \
                                   "requires 4 three type and 2 " \
                                   "two type, prior to" \
                                   " ability skill modifications"
                raise ValueError
        elif self.__char_type == "Sidekick":
            if self.type_count(skill_list, '3', '2') != [3, 3]:
                self.__error_msg = "Incorrect number of dice, Sidekick " \
                                   "requires 3 three type and 3 two type," \
                                   " prior to ability skill modifications"
                raise ValueError
        elif self.__char_type == "Ally":
            if self.type_count(skill_list, '2', '1') != [2, 4]:
                self.__error_msg = "Incorrect number of dice, Ally requires" \
                                   " 2 two type and 4 one type, prior " \
                                   "to ability skill modifications"
                raise ValueError
        else:
            if self.type_count(skill_list, '2', '1') != [0, 6]:
                self.__error_msg = "Incorrect number of dice, Follower " \
                                   "requires 6 one type dice, prior " \
                                   "to ability skill modifications"
                raise ValueError

    @staticmethod
    def type_count(skill_list, type_1, type_2):
        """
        - Counts the different occurrences of each input types in the provided
          skill list
        :param skill_list: list of skills inputted by the user
        :param type_1: first type of dice to be counted
        :param type_2: second type of dice to be counted
        :return: returns an array of the results, [type_one, type_two] format

        >>> IV=InputValidator()
        >>> IV.type_count(['b=3d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=2d6',
        ... 'c=2d6'], '3', '2')
        [4, 2]
        >>> IV.type_count(['b=1d10', 's=1d10', 'd=1d10', 'm=1d10',
        ... 'f=1d6', 'c=1d6'], '1', '')
        [6, 0]
        """
        type_one = 0
        type_two = 0
        for dice in skill_list:
            if dice[2] == type_1:
                type_one += 1
            elif dice[2] == type_2:
                type_two += 1
        return [type_one, type_two]

    def check_dice_type(self, skill_list):
        """
        - Checks the types of dice in the param skill_list, validates against
          character type
        :param skill_list: list of six skills provided by the user
        :return: raises ValueError is not valid types

        >>> IV=InputValidator()

        >>> IV.set_char_type("Follower")
        >>> IV.check_dice_type(str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
        ... 'f=2d6', 'c=2d6']).strip('[]'))

        >>> IV.set_char_type("Follower")
        >>> IV.check_dice_type(str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
        ... 'f=2d6', 'c=2d10']).strip('[]'))
        Traceback (most recent call last):
        ...
        ValueError
        """
        if self.__char_type == "Leader":
            if skill_list.count("d10") != 4 and skill_list.count("d8") != 2:
                self.__error_msg = "Incorrect number of dice" \
                                   " types for character type"
                raise ValueError
        elif self.__char_type == "Sidekick":
            if skill_list.count("d8") != 3 and skill_list.count("d6") != 3:
                self.__error_msg = "Incorrect number of dice " \
                                   "types for character type"
                raise ValueError
        else:
            if skill_list.count("d6") != 6:
                self.__error_msg = "Incorrect number of dice " \
                                   "types for character type"
                raise ValueError

    def set_char_type(self, type_value):
        self.__char_type = type_value

    def valid_output(self, string_list):
        skill_array = []
        for ski in self.remove_values('hbsmfc=', string_list[2:9]):
            skill_array.append(ski.split('d'))
        for index, skill in enumerate(skill_array):
            for ind, value in enumerate(skill):
                if value == '':
                    skill_array[index].pop(ind)
        return [[string_list[0], string_list[1]],
                skill_array,
                self.remove_values('+', string_list[9:])]

    @staticmethod
    def remove_values(char_list, string_list):
        string = " ".join(string_list)
        string = re.sub('[' + char_list + ']', '', string)
        return string.split(' ')
