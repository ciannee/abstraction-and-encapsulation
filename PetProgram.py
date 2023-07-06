# import pet class from pet file
from Pet import Pet

# ask user for pet name
pet_name = input("\n\033[92mWhat is the name of your pet? ")

# ask user for pet animal type
pet_animal_type = input ("\n\033[31mWhat is the animal type of your pet? ")

# ask user for pet age
pet_age = int(input("\n\033[93mWhat is the age of your pet? "))

# create a construction
pet = Pet(pet_name, pet_animal_type, pet_age)

# create an object
user_pet = Pet(pet_name, pet_animal_type, pet_age)

# print output
print ("\n\n\033[91mYour Pet's Information:")

# display pet name
name_input = print("\n\033[94mName: ", user_pet.get_name())
# display pet animal type
type_input = print("\n\033[36mAnimal Type: ", user_pet.get_animal_type())
# display pet age
age_input = print("\n\033[95mAge: ", user_pet.get_age())



