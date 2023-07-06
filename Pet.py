# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 9: Abstraction and Encapsulation

# create pet class
class Pet:

# create a constructor
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # set name method
    def set_name(self):
        self.__name = name

    # set animal type method
    def set_animal_type(self):
        self.__animal_type = animal_type

    # set age method
    def set_age(self):
        self.__age = age

    # get name method
    def get_name(self):
        return self.__name

    # get animal type method
    def get_animal_type(self):
        return self.__animal_type

    # get age method
    def get_age(self):
        return self.__age