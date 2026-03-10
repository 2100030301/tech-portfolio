"""
Q5. Create a class Temperature with:
•	instance attribute celsius
•	a static method to_fahrenheit(celsius)
•	an instance method show_conversion() that uses the static method to print both values.
"""

class Temperature:
    def __init__(self, celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print(f'Celsius : {self.celsius}')
        print(f'Farenheit : {fahrenheit}')

t = Temperature(9.8)
t.show_conversion()