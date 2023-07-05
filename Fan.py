# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 9: Abstraction and Encapsulation

# create fan class
class Fan:

# create three constants (slow, medium, fast)
    SLOW = 1
    MEDIUM = 2
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

# return speed of the fan
    def getSpeed(self):
        return self.__speed

# set speed of the fan
    def setSpeed(self):
        self.__speed = speed

# return radius of the fan
    def getRadius(self):
        return self.__radius

# set radius of the fan
    def setRadius(self):
        self.__radius = radius

# return color of the fan
    def getColor(self):
        return self.__color

# set color of the fan
    def setColor(self):
        self.__color = color
