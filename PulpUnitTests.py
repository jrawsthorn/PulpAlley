import unittest
from Pulp import *
from League import *
from Character import *
from PulpConsole import *


class MainTests(unittest.TestCase):

    def setUp(self):
        self.__my_pulp = Pulp()
        self.__my_league = self.__my_pulp.add_league("Justice League")
        self.__my_pulp_console = PulpConsole()

    def test_01(self):
        print("Test 1: Pulp class can produce a League")
        self.assertEqual(self.__my_league.get_name(), "Justice League")

    def test_02(self):
        print("Test 2: Pulp class can produce a Leader")
        a_character = self.__my_league.add_character(
            "Leader", "Singapore-Smith",
            1, 10, 3, 8, 3, 10, 3, 10, 2, 8, 3, 10, 2, 10)
        self.assertEqual(a_character.display_unit_test(),
                         "Leader Singapore-Smith h=1d10 b=3d8 "
                         "s=3d10 d=3d10 m=2d8 f=3d10 c=2d10")

    def test_03(self):
        print("Test 3: Pulp class can add abilities to a character")
        a_character = self.__my_league.add_character(
            "Leader", "Singapore-Smith",
            1, 10, 3, 8, 3, 10, 3, 10, 2, 8, 3, 10, 2, 10)
        a_character.add_ability("Sharp")
        a_character.add_ability("Deadeye")
        a_character.add_ability("Hardened-Veteran")
        self.assertEqual(a_character.display_unit_test(),
                         "Leader Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10 "
                         "m=2d8 f=3d10 c=2d10 +Sharp "
                         "+Deadeye +Hardened-Veteran")

    def test_04(self):
        print("Test 4: Pulp class can add the ability Agile to a character "
              "and adjust the Dodge skill appropriately")
        a_character = self.__my_league.add_character(
            "Leader", "Singapore-Smith",
            1, 10, 3, 8, 3, 10, 3, 10, 2, 8, 3, 10, 2, 10)
        a_character.add_ability("Agile")
        self.assertEqual(a_character.display_unit_test(),
                         "Leader Singapore-Smith h=1d10 b=3d8 "
                         "s=3d10 d=4d10 m=2d8 f=3d10 c=2d10 +Agile")

    def test_05(self):
        print("Test 5: PulpConsole class can add a League")
        self.__my_pulp_console.do_League("Justice League")
        a_league = self.__my_pulp_console.get_my_league()
        self.assertEqual(a_league.get_name(), "Justice League")

    def test_06(self):
        print("Test 6: PulpConsole class can add a Leader given a string "
              "(string splicing functions properly)")
        self.__my_pulp_console.do_League("Justice League")
        self.__my_pulp_console.create_leader(
            "Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10 m=2d8 f=3d10 "
            "c=2d10 +Sharp +Deadeye +Hardened-Veteran")
        a_league = self.__my_pulp_console.get_my_league()
        a_character = a_league.find_character("Singapore-Smith")
        self.assertEqual(a_character.display_unit_test(),
                         "Leader Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10"
                         " m=2d8 f=3d10 c=2d10 +Sharp "
                         "+Deadeye +Hardened-Veteran")

    def test_07(self):
        print("Test 7: PulpConsole class can avoid adding a Leader when user "
              "character definition disobeys dice rules")
        self.__my_pulp_console.do_League("Justice League")
        self.__my_pulp_console.create_leader(
            "Singapore-Smith h=1d10 b=10d8 s=3d10 d=3d10 m=2d8 f=3d10 "
            "c=2d10 +Sharp +Deadeye +Hardened-Veteran")
        a_league = self.__my_pulp_console.get_my_league()
        self.assertEqual(a_league.find_character("Singapore-Smith"), None)

    def test_08(self):
        print("Test 8: League class knows when a leader exists already")
        self.__my_pulp_console.do_League("Justice League")
        self.__my_pulp_console.create_leader(
            "Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10 m=2d8 f=3d10 c=2d10 "
            "+Sharp +Deadeye +Hardened-Veteran")
        a_league = self.__my_pulp_console.get_my_league()
        self.assertEqual(a_league.has_leader(), True)

    def test_09(self):
        print("Test 9: League class knows when a roster is full")
        self.__my_pulp_console.do_League("Justice League")
        self.__my_pulp_console.create_leader(
            "Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10 m=2d8 f=3d10 c=2d10 "
            "+Sharp +Deadeye +Hardened-Veteran")
        self.__my_pulp_console.create_sidekick(
            "Arge h=1d8 b=3d8 s=3d8 d=2d6 m=3d8 f=2d6 c=2d6 +Athletic +Fierce")
        self.__my_pulp_console.create_ally(
            "Enki h=1d6 b=2d6 s=2d6 d=1d6 m=1d6 f=1d6 c=1d6 +Marksman")
        self.__my_pulp_console.create_ally(
            "Kazak h=1d6 b=2d6 s=2d6 d=1d6 m=1d6 f=1d6 c=1d6 +Marksman")
        self.__my_pulp_console.create_ally(
            "Little-Skeet h=1d6 b=1d6 s=1d6 d=2d6 m=1d6 f=1d6 c=2d6 +Crafty")
        self.__my_pulp_console.create_follower(
            "Chu-Chu h=1d6 b=1d6 s=1d6 d=1d6 m=1d6 f=1d6 c=1d6 +Animal")
        a_league = self.__my_pulp_console.get_my_league()
        self.assertEqual(a_league.is_roster_full(), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
