# Create class that represents measurements units: Celcius, Farenheit, Centimeter, Inch, Kilometer, Mile, Liter, Gallon
# Create each class for listed units
# Create methods that allow convering units to each other Celcius <-> Fahrenheit, Centimeter <-> Inch, Kilometer <-> Mile, Liter <-> Gallon
# Create method that allows to compare units using logical expressions

# should to_SI return an unit object or just a value?
# value - less redundant stuff, easier to compare 
# unit object - will have info what it actually converts into - more readable, more consistent

from abc import ABC, abstractmethod, abstractproperty


RELATIVE_PRECISION = 0.0001


class Unit(ABC):
    @abstractproperty
    def symbol(self):
        pass

    @abstractproperty
    def unit_type(self):
        pass

    @abstractmethod
    def to_SI(self):
        pass

    def __init__(self, num_value):
        self.value = num_value

    def __str__(self):
        return f"{self.value}{self.symbol}"

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return abs(self.value - other.value) < RELATIVE_PRECISION * self.value
        elif hasattr(other, "to_SI") and self.unit_type == other.unit_type:
            return abs(self.to_SI().value - other.to_SI().value) < RELATIVE_PRECISION * self.value
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.value < other.value
        elif hasattr(other, "to_SI") and self.unit_type == other.unit_type:
            return self.to_SI().value - other.to_SI().value <= -RELATIVE_PRECISION * self.value
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return self.value > other.value
        elif hasattr(other, "to_SI") and self.unit_type == other.unit_type:
            return self.to_SI().value - other.to_SI().value >= RELATIVE_PRECISION * self.value
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other


class Celsius(Unit):
    symbol = "°C"
    unit_type = "temperature"

    def to_SI(self):
        value = self.value + 273.15
        return Kelvin(value)


    def to_fahrenheit(self):
        value = self.value * 1.8 + 32
        return Fahrenheit(value)


class Fahrenheit(Unit):
    symbol = "°F"
    unit_type = "temperature"

    def to_SI(self):
        value = 5 / 9 * self.value + 459.67
        return Kelvin(value)

    def to_celsius(self):
        value = (self.value - 32) * 0.5556
        return Celsius(value)


class Centimeter(Unit):
    symbol = " cm"
    unit_type = "length"

    def to_SI(self):
        value = self.value / 100
        return Meter(value)

    def to_inch(self):
        value = self.value / 2.54
        return Inch(value)


class Inch(Unit):
    symbol = "″"
    unit_type = "length"

    def to_SI(self):
        value = self.value * 0.0254
        return Meter(value)

    def to_centimeter(self):
        value = self.value * 2.54
        return Centimeter(value)


class Kilometer(Unit):
    symbol = "km"
    unit_type = "length"

    def to_SI(self):
        value = self.value * 1000
        return Meter(value)

    def to_mile(self):
        value = self.value * 0.62137
        return Mile(value)


class Mile(Unit):
    symbol = " mi."
    unit_type = "length"

    def to_SI(self):
        value = self.value * 1609.344
        return Meter(value)

    def to_kilometer(self):
        value = self.value * 1.60934
        return Kilometer(value)


class Liter(Unit):
    symbol = " l"
    unit_type = "volume"

    def to_SI(self):
        value = self.value / 1000
        return CubicMeter(value)

    def to_gallon(self):
        value = self.value * 0.264172
        return Gallon(value)


class Gallon(Unit):
    symbol = " gal"
    unit_type = "volume"

    def to_SI(self):
        value = self.value * 0.003785
        return CubicMeter(value)

    def to_liter(self):
        value = self.value * 3.785412
        return Liter(value)


# Base units
class Kelvin(Unit):
    symbol = " K"
    unit_type = "temperature"

    def to_SI(self):
        return self


class Meter(Unit):
    symbol = " m"
    unit_type = "length"

    def to_SI(self):
        return self


class CubicMeter(Unit):
    symbol = " m^3"
    unit_type = "volume"

    def to_SI(self):
        return self
