#! python

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Initial temperature

    @property
    def celsius(self):
        return self._celsius  # Getter: returns the current temperature

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:  # Validating the new temperature
            self._celsius = value  # Setter: updates the temperature
        else:
            raise ValueError("Temperature must be above absolute zero")  # Error if value is invalid
        
if __name__ == '__main__':
    
    my_temp = Temperature(30)
    print(my_temp.celsius)
    my_temp.celsius = -300
    print(my_temp.celsius)