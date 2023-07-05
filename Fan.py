# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 9: Abstraction and Encapsulation

# create fan class
class Fan:

# create three constants (slow, medium, fast)
    SLOW = 1
    MEDIUM = 1
    FAST = 3

# create a constructor (speed, radius, color, switch)
    def __init__(self, speed = SLOW, radius = 5, color = 'blue', switch = False):
    # behavior (instance methods)
    self.__speed = speed
    self.__radius = radius
    self.__color = color
    self.__switch = switch

# turns on fan
    def turnOn(self):
        self.__switch = True

# turns off fan
    def turnOff(self):
        self.__switch = False



