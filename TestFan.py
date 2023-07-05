
# import Fan from Fan file
from Fan import Fan

# create two fan objects
class TestFan:
    def __init__(self):
        # first fan
        first_fan = Fan(Fan, FAST, 10, "yellow", True)
        # second fan
        second_fan = Fan(Fan, MEDIUM, 5, "blue", False)

# print output
print ("\n")
print("First Fan: ", first_fan.speed )