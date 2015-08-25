import cmd
import string
import sys
from Pulp import *
from League import *
from InputValidator import *
from MyException import *


class PulpConsole(cmd.Cmd):

    def __init__(self):
        self.__my_pulp = Pulp()
        self.__my_league = None
        self.__my_input_validator = InputValidator()
        cmd.Cmd.__init__(self)
        self.prompt = 'Pulp > '

    def get_my_league(self):
        return self.__my_league

    def create_leader(self, argument):

        try:
            if self.__my_league.has_leader() is True:
                raise MyException("League already has a Leader.")
            elif self.__my_league.is_roster_full() is True:
                raise MyException("League roster is full.")
            else:
                argument = "Leader " + argument
                validator_output = \
                    self.__my_input_validator.process_input(argument)
                if validator_output is None:
                    raise MyException("")
        except MyException as err:
            print(err)
            print("No Leader created.")
        else:
            name = validator_output[0][1]
            skills_array = validator_output[1]
            abilities_array = validator_output[2]
            a_character = self.__my_league.add_character(
                "Leader", name,
                int(skills_array[0][0]), int(skills_array[0][1]),
                int(skills_array[1][0]), int(skills_array[1][1]),
                int(skills_array[2][0]), int(skills_array[2][1]),
                int(skills_array[3][0]), int(skills_array[3][1]),
                int(skills_array[4][0]), int(skills_array[4][1]),
                int(skills_array[5][0]), int(skills_array[5][1]),
                int(skills_array[6][0]), int(skills_array[6][1]))
            for ability in abilities_array:
                a_character.add_ability(ability)
            print("Leader created: " + a_character.get_name())

    def create_sidekick(self, argument):

        try:
            if self.__my_league.has_sidekick() is True:
                raise MyException("League already has a Sidekick.")
            elif self.__my_league.is_roster_full() is True:
                raise MyException("League roster is full.")
            else:
                argument = "Sidekick " + argument
                validator_output = \
                    self.__my_input_validator.process_input(argument)
                if validator_output is None:
                    raise MyException("")
        except MyException as err:
            print(err)
            print("No Sidekick created.")
        else:
            name = validator_output[0][1]
            skills_array = validator_output[1]
            abilities_array = validator_output[2]
            a_character = self.__my_league.add_character(
                "Sidekick", name,
                int(skills_array[0][0]), int(skills_array[0][1]),
                int(skills_array[1][0]), int(skills_array[1][1]),
                int(skills_array[2][0]), int(skills_array[2][1]),
                int(skills_array[3][0]), int(skills_array[3][1]),
                int(skills_array[4][0]), int(skills_array[4][1]),
                int(skills_array[5][0]), int(skills_array[5][1]),
                int(skills_array[6][0]), int(skills_array[6][1]))
            for ability in abilities_array:
                a_character.add_ability(ability)
            print("Sidekick created: " + a_character.get_name())

    def create_ally(self, argument):
        try:
            if self.__my_league.is_roster_full() is True:
                raise MyException("League roster is full.")
            else:
                argument = "Ally " + argument
                validator_output = \
                    self.__my_input_validator.process_input(argument)
                if validator_output is None:
                    raise MyException("")
        except MyException as err:
            print(err)
            print("No Ally created.")
        else:
            name = validator_output[0][1]
            skills_array = validator_output[1]
            abilities_array = validator_output[2]
            a_character = self.__my_league.add_character(
                "Ally", name,
                int(skills_array[0][0]), int(skills_array[0][1]),
                int(skills_array[1][0]), int(skills_array[1][1]),
                int(skills_array[2][0]), int(skills_array[2][1]),
                int(skills_array[3][0]), int(skills_array[3][1]),
                int(skills_array[4][0]), int(skills_array[4][1]),
                int(skills_array[5][0]), int(skills_array[5][1]),
                int(skills_array[6][0]), int(skills_array[6][1]))
            for ability in abilities_array:
                a_character.add_ability(ability)
            print("Ally created: " + a_character.get_name())

    def create_follower(self, argument):
        try:
            if self.__my_league.is_roster_full() is True:
                raise MyException("League roster is full.")
            else:
                argument = "Follower " + argument
                validator_output = \
                    self.__my_input_validator.process_input(argument)
                if validator_output is None:
                    raise MyException("")
        except MyException as err:
            print(err)
            print("No Follower created.")
        else:
            name = validator_output[0][1]
            skills_array = validator_output[1]
            abilities_array = validator_output[2]
            a_character = self.__my_league.add_character(
                "Follower", name,
                int(skills_array[0][0]), int(skills_array[0][1]),
                int(skills_array[1][0]), int(skills_array[1][1]),
                int(skills_array[2][0]), int(skills_array[2][1]),
                int(skills_array[3][0]), int(skills_array[3][1]),
                int(skills_array[4][0]), int(skills_array[4][1]),
                int(skills_array[5][0]), int(skills_array[5][1]),
                int(skills_array[6][0]), int(skills_array[6][1]))
            for ability in abilities_array:
                a_character.add_ability(ability)
            print("Follower created: " + a_character.get_name())

    def do_League(self, argument):
        a_league = self.__my_pulp.add_league(argument)
        self.__my_league = a_league
        self.__my_league.display()

    def help_League(self):
        print("syntax: League [name]",)
        print("-- creates a league \n")
        print("   A league consists of various characters. Each league "
              "must include one (and only one) Leader.")
        print("   A Leader may or may not be accompanied by a single "
              "Sidekick. A League may include many Allies and Followers.")
        print("   The number of characters is determined by filling a "
              "league roster. A roster has a maximum of 10 slots.")
        print("   A Leader does not take any slots on the roster. A "
              "Sidekick takes 3 slots. An Ally takes 2 slots. A "
              "Follower takes 1 slot.")
        print("   Players are encouraged to include 4 to 6 characters "
              "in their first Leagues.")

    def do_Leader(self, argument):
        if self.__my_league is not None:
            self.create_leader(argument)
        else:
            print("No league exists yet. Leader not created.")

    def help_Leader(self):
        print("syntax: Leader [name]",)
        print("-- creates a Leader")

    def do_Sidekick(self, argument):
        if self.__my_league is not None:
            self.create_sidekick(argument)
        else:
            print("No league exists yet. Sidekick not created.")

    def help_Sidekick(self):
        print("syntax: Sidekick [name]",)
        print("-- creates a Sidekick")

    def do_Ally(self, argument):
        if self.__my_league is not None:
            self.create_ally(argument)
        else:
            print("No league exists yet. Ally not created.")

    def help_Ally(self):
        print("syntax: Ally [name]",)
        print("-- creates an Ally")

    def do_Follower(self, argument):
        if self.__my_league is not None:
            self.create_follower(argument)
        else:
            print("No league exists yet. Follower not created.")

    def help_Follower(self):
        print("syntax: Follower [name]",)
        print("-- creates a Follower")

    def do_Display(self, argument):
        if self.__my_league is not None:
            self.__my_league.display()
        else:
            print("No league exists yet.")

    def help_Display(self):
        print("syntax: display",)
        print("-- displays a league")

    def do_Quit(self, arg):
        sys.exit(1)

    def help_Quit(self):
        print("syntax: quit",)
        print("-- terminates the console")
