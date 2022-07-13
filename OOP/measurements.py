# Create class that represents measurements units: Celcius, Farenheit, Centimeter, Inch, Kilometer, Mile, Liter, Gallon
# Create each class for listed units
# Create methods that allow convering units to each other Celcius <-> Fahrenheit, Centimeter <-> Inch, Kilometer <-> Mile, Liter <-> Gallon
# Create method that allows to compare units using logical expressions

class Unit:
    symbol = None

    def __init__(self, num_value):
        self.value = num_value

    def __str__(self):
        return f"{self.value}{self.symbol}"


class Celsius(Unit):
    symbol = "°C"

    def to_fahrenheit(self):
        value = self.value * 1.8 + 32
        return Fahrenheit(value)

    def __eq__(self, other):
        if isinstance(other, Celsius):
            return self.value == other.value
        elif isinstance(other, Fahrenheit):
            return abs(self.value - other.to_celsius().value) < 0.01
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Celsius):
            return self.value < other.value
        elif isinstance(other, Fahrenheit):
            return self.value - other.to_celsius().value <= -0.01
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if isinstance(other, Celsius):
            return self.value > other.value
        elif isinstance(other, Fahrenheit):
            return self.value - other.to_celsius().value >= 0.01
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other

    
class Fahrenheit(Unit):
    symbol = "°F"

    def to_celsius(self):
        value = (self.value - 32) * 0.5556
        return Celsius(value)


class Centimeter(Unit):
    symbol = " cm"

    def to_inch(self):
        value = self.value / 2.54
        return Inch(value)


class Inch(Unit):
    symbol = "″"

    def to_centimeter(self):
        value = self.value * 2.54
        return Centimeter(value)


class Kilometer(Unit):
    symbol = "km"

    def to_mile(self):
        value = self.value * 0.62137
        return Mile(value)


class Mile(Unit):
    symbol = " mi."

    def to_kilometer(self):
        value = self.value * 1.60934
        return Kilometer(value)


class Liter(Unit):
    symbol = " l"

    def to_gallon(self):
        value = self.value * 0.264172
        return Gallon(value)


class Gallon(Unit):
    symbol = " gal"

    def to_liter(self):
        value = self.value * 3.785412
        return Liter(value)

