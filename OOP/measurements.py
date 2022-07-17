# Create class that represents measurements units: Celcius, Farenheit, Centimeter, Inch, Kilometer, Mile, Liter, Gallon
# Create each class for listed units
# Create methods that allow convering units to each other Celcius <-> Fahrenheit, Centimeter <-> Inch, Kilometer <-> Mile, Liter <-> Gallon
# Create method that allows to compare units using logical expressions

COMPARISON_PRECISION = 0.01


class Unit:
    symbol = None

    def __init__(self, num_value):
        self.value = num_value

    def __str__(self):
        return f"{self.value}{self.symbol}"

    # Comparisons should work for all units that can convert into each other
    def __eq__(self, other):
        if type(self) == type(other):
            return abs(self.value - other.value) < COMPARISON_PRECISION
        elif hasattr(other, self.converting_function):
            convert = getattr(other, self.converting_function)
            return abs(self.value - convert().value) < COMPARISON_PRECISION
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if type(self) == type(other):
            return self.value < other.value
        elif hasattr(other, self.converting_function):
            convert = getattr(other, self.converting_function)
            return self.value - convert().value <= -COMPARISON_PRECISION
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if type(self) == type(other):
            return self.value > other.value
        elif hasattr(other, self.converting_function):
            convert = getattr(other, self.converting_function)
            return self.value - convert().value >= COMPARISON_PRECISION
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other


class Celsius(Unit):
    symbol = "°C"
    converting_function = "to_celsius"

    def to_fahrenheit(self):
        value = self.value * 1.8 + 32
        return Fahrenheit(value)


class Fahrenheit(Unit):
    symbol = "°F"
    converting_function = "to_fahrenheit"

    def to_celsius(self):
        value = (self.value - 32) * 0.5556
        return Celsius(value)


class Centimeter(Unit):
    symbol = " cm"
    converting_function = "to_centimeter"

    def to_inch(self):
        value = self.value / 2.54
        return Inch(value)


class Inch(Unit):
    symbol = "″"
    converting_function = "to_inch"

    def to_centimeter(self):
        value = self.value * 2.54
        return Centimeter(value)


class Kilometer(Unit):
    symbol = "km"
    converting_function = "to_kilometer"

    def to_mile(self):
        value = self.value * 0.62137
        return Mile(value)


class Mile(Unit):
    symbol = " mi."
    converting_function = "to_mile"

    def to_kilometer(self):
        value = self.value * 1.60934
        return Kilometer(value)


class Liter(Unit):
    symbol = " l"
    converting_function = "to_liter"

    def to_gallon(self):
        value = self.value * 0.264172
        return Gallon(value)


class Gallon(Unit):
    symbol = " gal"
    converting_function = "to_gallon"

    def to_liter(self):
        value = self.value * 3.785412
        return Liter(value)
