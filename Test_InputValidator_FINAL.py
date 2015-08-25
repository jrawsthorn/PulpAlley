from unittest import TestCase
from InputValidator import *
__author__ = 'JRaw'


class TestInputValidator(TestCase):

    def setUp(self):
        self.IV = InputValidator()

    def tearDown(self):
        print("down")

    def test_process_input_1(self):
        self.IV.set_char_type("")
        self.assertEqual(self.IV.process_input(999), "Invalid command/syntax: "
                                                     "Input is not a string")

    def test_process_input_2(self):
        input_string = "Leader Singapore-Smith h=1d10 b=3d8 s=3d10 d=3d10 " \
                       "m=2d8 f=3d10 c=2d10 +Sharp +Deadeye +Hardened-Veteran"
        return_array = [['Leader', 'Singapore-Smith'],
                        [['1', '10'], ['3', '8'],
                         ['3', '10'], ['3', '10'],
                         ['2', '8'], ['3', '10'], ['2', '10']],
                        ['Sharp', 'Deadeye', 'Hardened-Veteran']]
        self.assertEqual(self.IV.process_input(input_string), return_array)

    def test_process_input_3(self):
        input_string = "Sidekick Arge h=1d8 b=3d8 s=3d8 d=2d6 m=3d8 " \
                       "f=2d6 c=2d6 +Athletic +Fierce"
        return_array = [['Sidekick', 'Arge'],
                        [['1', '8'], ['3', '8'],
                         ['3', '8'], ['2', '6'],
                         ['3', '8'], ['2', '6'], ['2', '6']],
                        ['Athletic', 'Fierce']]
        self.assertEqual(self.IV.process_input(input_string), return_array)

    def test_process_input_4(self):
        input_string = "Ally Enki h=1d6 b=2d6 s=2d6 d=1d6 m=1d6 " \
                       "f=1d6 c=1d6 +Marksman"
        return_array = [['Ally', 'Enki'],
                        [['1', '6'], ['2', '6'],
                         ['2', '6'], ['1', '6'],
                         ['1', '6'], ['1', '6'], ['1', '6']],
                        ['Marksman']]
        self.assertEqual(self.IV.process_input(input_string), return_array)

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
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_type("Leaderr"))

    def test_has_valid_type_7(self):
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_type("leader"))

    def test_has_valid_type_8(self):
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_type("leader"))

    def test_has_valid_type_9(self):
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_type("sidekick"))

    def test_has_valid_type_10(self):
        self.assertRaises(ValueError, lambda: self.IV.has_valid_type("ally"))

    def test_has_valid_type_11(self):
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_type("follower"))

    def test_has_valid_name_1(self):
        self.assertRaises(
            ValueError,
            lambda: self.IV.has_valid_name("Example name is too long"))

    def test_has_valid_name_2(self):
        self.assertEqual(self.IV.has_valid_name("Good length name"), None)

    def test_has_valid_health_1(self):
        self.IV.set_char_type("Leader")
        self.assertEqual(self.IV.has_valid_health("h=1d10"), None)

    def test_has_valid_health_2(self):
        self.IV.set_char_type("Sidekick")
        self.assertEqual(self.IV.has_valid_health("h=1d8"), None)

    def test_has_valid_health_3(self):
        self.IV.set_char_type("Leader")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_health("h=1d8"))

    def test_has_valid_health_4(self):
        self.IV.set_char_type("Sidekick")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_health("h=1d6"))

    def test_has_valid_health_5(self):
        self.IV.set_char_type("Follower")
        self.assertEqual(self.IV.has_valid_health("h=1d6"), None)

    def test_has_valid_health_6(self):
        self.IV.set_char_type("Ally")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_health("h=1d10"))

    def test_has_valid_health_7(self):
        self.IV.set_char_type("Follower")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_health("h=1d10"))

    def test_has_valid_skills_1(self):
        self.IV.set_char_type("Leader")
        skill_list = ['b=3d8', 's=3d10', 'd=3d10', 'm=2d8', 'f=3d10', 'c=2d10']
        self.assertEquals(self.IV.has_valid_skills(skill_list), None)

    def test_has_valid_skills_2(self):
        self.IV.set_char_type("Sidekick")
        skill_list = ['b=2d8', 's=3d8', 'd=3d6', 'm=2d8', 'f=3d6', 'c=2d6']
        self.assertEquals(self.IV.has_valid_skills(skill_list), None)

    def test_has_valid_skills_3(self):
        self.IV.set_char_type("Ally")
        skill_list = ['b=2d6', 's=2d6', 'd=1d6', 'm=1d6', 'f=1d6', 'c=1d6']
        self.assertEquals(self.IV.has_valid_skills(skill_list), None)

    def test_has_valid_skills_4(self):
        self.IV.set_char_type("Follower")
        skill_list = ['b=1d6', 's=1d6', 'd=1d6', 'm=1d6', 'f=1d6', 'c=1d6']
        self.assertEquals(self.IV.has_valid_skills(skill_list), None)

    def test_has_valid_skills_5(self):
        self.IV.set_char_type("Leader")
        skill_list = ['b=2d6', 's=2d6', 'd=1d6', 'm=1d6', 'f=1d6', 'c=1d6']
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_skills(skill_list))

    def test_has_valid_skills_6(self):
        self.IV.set_char_type("Leader")
        skill_list = ['b=3d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=1d6', 'c=2d6']
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_skills(skill_list))

    def test_has_valid_abilities_1(self):
        self.IV.set_char_type("Leader")
        self.assertEquals(
            self.IV.has_valid_abilities(
                ['+Sharp', '+Deadeye', '+Quick-Shot']), None)

    def test_has_valid_abilities_2(self):
        self.IV.set_char_type("Sidekick")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(
                ['+Sharp', '+Deadeye', '+Quick-Shot']))

    def test_has_valid_abilities_3(self):
        self.IV.set_char_type("Ally")
        self.assertEquals(self.IV.has_valid_abilities(['+Sharp']), None)

    def test_has_valid_abilities_4(self):
        self.IV.set_char_type("Ally")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(
                ['+Sharp', '+Deadeye']))

    def test_has_valid_abilities_5(self):
        self.IV.set_char_type("Ally")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(['+Quick-Shot']))

    def test_has_valid_abilities_6(self):
        self.IV.set_char_type("Follower")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(['+Deadeye']))

    def test_has_valid_abilities_7(self):
        self.IV.set_char_type("Sidekick")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(
                ['+Deadeye', '+Deadeye']))

    def test_has_valid_abilities_8(self):
        self.IV.set_char_type("Leader")
        self.assertRaises(
            ValueError, lambda: self.IV.has_valid_abilities(
                ['+Sharp', '+Deadeye', '+Quick-Shot', '+Hardened-Veteran']))

    def test_check_dice_count_1(self):
        skill_list = ['b=3d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=2d6', 'c=2d6']
        self.IV.set_char_type("Leader")
        self.assertEquals(self.IV.check_dice_count(skill_list), None)

    def test_check_dice_count_2(self):
        skill_list = ['b=3d10', 's=3d10', 'd=3d10', 'm=2d10', 'f=2d6', 'c=2d6']
        self.IV.set_char_type("Sidekick")
        self.assertEquals(self.IV.check_dice_count(skill_list), None)

    def test_check_dice_count_3(self):
        skill_list = ['b=2d10', 's=2d10', 'd=1d10', 'm=1d10', 'f=1d6', 'c=1d6']
        self.IV.set_char_type("Ally")
        self.assertEquals(self.IV.check_dice_count(skill_list), None)

    def test_check_dice_count_4(self):
        skill_list = ['b=1d10', 's=1d10', 'd=1d10', 'm=1d10', 'f=1d6', 'c=1d6']
        self.IV.set_char_type("Follower")
        self.assertEquals(self.IV.check_dice_count(skill_list), None)

    def test_check_dice_count_5(self):
        skill_list = ['b=1d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=2d6', 'c=2d6']
        self.IV.set_char_type("Leader")
        self.assertRaises(
            ValueError, lambda: self.IV.check_dice_count(skill_list))

    def test_check_dice_count_6(self):
        skill_list = ['b=4d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=2d6', 'c=2d6']
        self.IV.set_char_type("Ally")
        self.assertRaises(
            ValueError, lambda: self.IV.check_dice_count(skill_list))

    def test_type_count_1(self):
        skill_list = ['b=3d10', 's=3d10', 'd=3d10', 'm=3d10', 'f=2d6', 'c=2d6']
        self.assertEquals(self.IV.type_count(skill_list, '3', '2'), [4, 2])

    def test_type_count_2(self):
        skill_list = ['b=1d10', 's=1d10', 'd=1d10', 'm=1d10', 'f=1d6', 'c=1d6']
        self.assertEquals(self.IV.type_count(skill_list, '1', ''), [6, 0])

    def test_check_dice_type_1(self):
        skill_list = str(['b=3d10', 's=3d10', 'd=3d10', 'm=3d10',
                          'f=2d8', 'c=2d8']).strip('[]')
        self.IV.set_char_type("Leader")
        self.assertEquals(self.IV.check_dice_type(skill_list), None)

    def test_check_dice_type_2(self):
        skill_list = str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
                          'f=2d6', 'c=2d6']).strip('[]')
        self.IV.set_char_type("Follower")
        self.assertEquals(self.IV.check_dice_type(skill_list), None)

    def test_check_dice_type_3(self):
        skill_list = str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
                          'f=2d6', 'c=2d6']).strip('[]')
        self.IV.set_char_type("Ally")
        self.assertEquals(self.IV.check_dice_type(skill_list), None)

    def test_check_dice_type_4(self):
        skill_list = str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
                          'f=2d6', 'c=2d10']).strip('[]')
        self.IV.set_char_type("Follower")
        self.assertRaises(
            ValueError, lambda: self.IV.check_dice_type(skill_list))

    def test_check_dice_type_5(self):
        skill_list = str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
                          'f=2d6', 'c=2d10']).strip('[]')
        self.IV.set_char_type("Leader")
        self.assertRaises(
            ValueError, lambda: self.IV.check_dice_type(skill_list))

    def test_check_dice_type_6(self):
        skill_list = str(['b=3d6', 's=3d6', 'd=3d6', 'm=3d6',
                          'f=2d6', 'c=2d10']).strip('[]')
        self.IV.set_char_type("Ally")
        self.assertRaises(
            ValueError, lambda: self.IV.check_dice_type(skill_list))
