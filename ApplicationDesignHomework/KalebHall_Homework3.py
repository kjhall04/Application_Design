#! python3
# Homework 3 - Kaleb Hall

class Car:
    # Initializer / Instance Attributes
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    # Another instance method
    def typeofcar(self):
        return f"The car model is {self.model}."
    
    # Instance method
    def description(self):
        return f"The color of the car is {self.color}"
    
# main function
if __name__ == '__main__':

    # Creating an object
    my_car = Car('Grey', '2017 Ford Fusion')

    # Accessing attributes and methods
    print(my_car.typeofcar())  # car is the color grey
    print(my_car.description())  # car is a ford fusion