# This program is for showing how varables and names work in Python
cars=100
space_in_car=4.0
drivers=30
passangers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passangers_per_car=passangers/cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven,"cars empty today")
print("We can transport", carpool_capacity, "people today")
print("We have", passangers, "passangers to carpool today")
print("We need to put about", average_passangers_per_car, "passangers per car")
