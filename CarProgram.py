# import Car class from Car file
from Car import Car

# create car object
car = Car(2023, "Honda Civic Sedan")

# call acceleration five times
for i in range(1,6):
    car.accelerate()
# get the current speed and display
    car_speed = print("\033[01m\033[92mThe Current Speed of the Car is: ", "\n", car.get_speed())

# call brake method five times
for i in range(1,6):
    car.brake()
# get the current speed and display