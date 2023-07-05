
# import Fan from Fan file
from Fan import Fan

# create two fan objects
class TestFan:
    # first fan
    first_fan = Fan(FAST, 10, "yellow", True)
    # second fan
    second_fan = Fan(MEDIUM, 5, "blue", False)

# print output
print ("\n")
first_fan = print("\033[36mFirst Fan: ", "\n\nSpeed: ", first_fan.speed)