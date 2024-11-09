class Circle():
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


class CalculateCircleLengthMixin:
   def calculate_length(self):
       return (2 * self._pi * self._radius)

   def __lt__(self, other):
       return self


class CircleWithMixin(Circle, CalculateCircleLengthMixin):
   pass


class Counter():
    def __init__(self, value):
        self._value = value
    def __lt__(self, other):
        return self._value < other._value


if __name__ == '__main__':
    print(Counter(5) > Counter(10))

