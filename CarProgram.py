# import Car class from Car file
from Car import Car
import time

# create car object
car = Car(2023, "Honda Civic Sedan")

# call acceleration five times
print("\nAccelerate:")
for i in range(1,6):
    car.accelerate()
# get the current speed and display
    time.sleep(2)
    car_accelerate = print("\n\033[01m\033[92mThe Current Speed of the Car is: ", "\n", car.get_speed())

# call brake method five times
print("\n\n\033[01m\033[34mBrake")
for i in range(1,6):
    car.brake()
# get the current speed and display
    time.sleep(2)
    car_brake = print("\n\n\033[01m\033[34mThe Current Speed of the Car is: ", "\n", car.get_speed())