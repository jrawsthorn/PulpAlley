from unittest import TestCase
from InputValidator import *

__author__ = 'JRaw'


class TestInputValidator(TestCase):
    IV = InputValidator()

    def test_process_input(self):
        self.IV.set_char_type("")
        self.assertEqual(self.IV.process_input(999), "Invalid command/syntax: Input is not a string")

    def test_has_valid_type_1(self):
        self.assertEqual(self.IV.has_valid_type("Leader"), None)

    def test_has_valid_type_2(self):
        self.assertEqual(self.IV.has_valid_type("Sidekick"), None)

    def test_has_valid_type_3(self):
        self.assertEqual(self.IV.has_valid_type("Ally"), None)

    def test_has_valid_type_4(self):
        self.assertEqual(self.IV.has_valid_type("Follower"), None)

    def test_has_valid_type_5(self):
        self.assertEqual(self.IV.has_valid_type("    Follower    "), None)

    def test_has_valid_type_6(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("Leaderr"))

    def test_has_valid_type_7(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("leader"))

    def test_has_valid_type_8(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("leader"))

    def test_has_valid_type_9(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("sidekick"))

    def test_has_valid_type_10(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("ally"))

    def test_has_valid_type_11(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("follower"))

    def test_has_valid_name_1(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_name("Example name is too long"))

    def test_has_valid_name_2(self):
        self.assertEqual(self.IV.has_valid_name("Good length name"), None)

    def test_has_valid_health_1(self):
        self.IV.set_char_type("Leader")

    def test_has_valid_health_2(self):
        self.assertEqual(self.IV.has_valid_health("h=d10"), None)

    def test_has_valid_health_3(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_health("h=d8"))

    def test_has_valid_health_4(self):
        self.IV.set_char_type("Sidekick")

    def test_has_valid_health_5(self):
        self.assertEqual(self.IV.has_valid_health("h=d8"), None)

    def test_has_valid_health_6(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_health("h=d6"))

    def test_has_valid_health_7(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_health("g=d6"))
'''
    def test_has_valid_skills(self):
        self.fail()

    def test_has_valid_abilities(self):
        self.fail()

    def test_check_dice_count(self):
        self.fail()

    def test_type_count(self):
        self.fail()

    def test_check_dice_type(self):
        self.fail()
'''