class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2

class SemiCircle(Circle):
    def __init__(self, diameter, radius):
        super().__init__(radius)
        self._diameter = diameter
    def calculate_area(self):
        return (super().calculate_area() / 2)
    @property
    def diameter(self):
        return self._diameter

if __name__ == '__main__':
    semi_circle = SemiCircle(4, 2)
    print(semi_circle.calculate_area())
    print(semi_circle.diameter)