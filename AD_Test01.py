class Robot:

    # Class Attribute

    type = "Automaton"

 

    # Initializer / Instance Attributes

    def __init__(self, model, year):

        self.model = model

        self.year = year

   

    # Instance method

    def description(self):

        return f"{self.model} is from the year {self.year}"

   

    # Another instance method

    def speak(self, message):

        return f"{self.model} says {message}"
    
if __name__ == '__main__':
    robot = Robot('Roomba', '2024')

    print(robot.description())
    print(robot.speak('Hello, World'))