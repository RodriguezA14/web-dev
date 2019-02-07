# Sets the number of cars to 100
cars = 100
# Sets the space in the car to 4.0
space_in_car = 4.0
# Sets the number of drivers to 30
drivers = 30
# Sets the number of passengers to 90
passengers = 90
# Calculates the number of cars that are not driven by subtracting the number of drivers from the total number of cars
cars_not_driven = cars - drivers
# Sets the number of cars driven to the number of cars
cars_driven = drivers
# Calculates the carpool capacity by multiplying the space in each car by the number of cars
carpool_capacity = cars_driven  * space_in_car
# Calculates the average number of passengers per car by dividing the number of passengers by the cars that are driven
average_passengers_per_car = passengers / cars_driven

# Outputs the number of cars
print("There are", cars, "cars available.")
# Outputs the number of files
print("There are only", drivers, "drivers available.")
# Outputs the number of cars that won't be driven
print("There will be", cars_not_driven, "empty cars today.")
# Outputs the carpool capacity
print("We can transport", carpool_capacity, "people today.")
# Outputs the number of passengers
print("We have", passengers, "to carpool today.")
# Outputs the average number of passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")