class Temperature:
    normal_temperature = 0
    def __init__(self, celcius):
        self._celcius = celcius

    @property
    def celcius(self):
        return self._celcius

    @celcius.setter
    def celcius(self, value):
        if value < -273 or value > 273:
            self._celcius = 0
        else:
            self._celcius = value
    @staticmethod
    def print_temperature_class():
        print("I am class temperature")
        pass
    @classmethod
    def calculate_temperature(cls, celcius):
        return cls.normal_temperature + celcius

if __name__ == "__main__":
    temperature = Temperature(10)
    temperature.celcius = -1000
    print(temperature.celcius)

    Temperature.print_temperature_class()
    print(Temperature.calculate_temperature(10))
