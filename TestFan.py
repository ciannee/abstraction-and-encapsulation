
# import Fan from Fan file
from Fan import Fan
import time
time.sleep(2)

# create two fan objects
fan1 = Fan("FAST", 10, "yellow", True)
fan2 = Fan("MEDIUM", 5, "blue", False)

# print output
print("\n")
fan1 = print("\033[01m\033[92mFirst Fan: ", "\n", fan1.getSpeed(), "\n", fan1.getRadius(), "\n", fan1.getColor())
fan2 = print("\n\n\033[01m\033[34mSecond Fan: ", "\n", fan2.getSpeed(), "\n", fan2.getRadius(), "\n", fan2.getColor())
print ("\n")