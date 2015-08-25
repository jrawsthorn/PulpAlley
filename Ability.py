class Ability:
    def __init__(self, level, name, description):
        self.__level = int(level)
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def display_unit_test(self):
        return self.__name
