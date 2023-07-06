# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 9: Abstraction and Encapsulation

# create car class
class Car: 
# create a constructor (model, make, speed)
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # make accelerate method
    def accelerate(self):
        self.__speed += 5

    # make brake method
    def brake(self):
        self.__speed -= 5

    # get speed method
    def get_speed(self):
        return self.__speed