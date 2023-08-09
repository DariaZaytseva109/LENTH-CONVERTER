from functools import total_ordering
from typing import Any

@total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1  # Отношение определяемой единицы измерения к миллиметрам

    def __init__(self, value) -> None:
        if type(value) == int:
            self._value = float(value)
        elif type(value) == float:
            self._value = value
        else:
            self._value = float(value.as_millimeters() / self.ratio)

    def __repr__(self) -> str:
        return (f'{type(self).__name__}({self._value})') # 'Inch(9.2332)'

    def as_millimeters(self) -> float:
        return round(self._value * self.ratio, 5)

    def __add__(self, argument):
        return self.__class__((self.as_millimeters() + argument.as_millimeters()) / self.ratio)

    def __sub__(self, argument):
        return self.__class__((self.as_millimeters() - argument.as_millimeters()) / self.ratio)

    def __mul__(self, argument):
        return self.__class__((self.as_millimeters() * argument.as_millimeters()) / self.ratio**2)

    def __truediv__(self, argument):
        return self.__class__((self.as_millimeters() / argument.as_millimeters()))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __le__(self, other):
        return (self.as_millimeters()) <= (other.as_millimeters())

    def __lt__(self, other):
        return (self.as_millimeters()) < (other.as_millimeters())

    def __hash__(self):
       return hash(self.as_millimeters())

    def __int__(self):
        return int(self.as_millimeters())
    def __float__(self):
        return float(self.as_millimeters())
class Centimeter(Millimeter):
    label = 'см'
    ratio = 10

    def __init__(self, value) -> None:
        super().__init__(value)
class Meter(Millimeter):
    label = 'метр'
    ratio = 1000

    def __init__(self, value) -> None:
        super().__init__(value)

class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4

    def __init__(self, value) -> None:
        super().__init__(value)

