import pytest

from measurements import (
    Celsius,
    Fahrenheit,
    Centimeter,
    Inch,
    Kilometer,
    Mile,
    Liter,
    Gallon,
)


class TestCelsiusAndFahrenheit:
    def test_create_celsius(self):
        temp = Celsius(33)
        assert temp.value == 33
        assert str(temp) == "33°C"

    def test_create_fahrenheit(self):
        temp = Fahrenheit(70.7)
        assert temp.value == 70.7
        assert str(temp) == "70.7°F"

    def test_convert_celsius_to_fahrenheit(self):
        temp = Celsius(1000)
        temp_f = temp.to_fahrenheit()
        assert isinstance(temp_f, Fahrenheit)
        assert temp_f.value == 1832

    def test_compare_celcius_equal(self):
        temp = Celsius(22)
        temp2 = Celsius(22)
        temp3 = Celsius(30)
        assert temp == temp2
        assert not temp == temp3

    def test_celsius_less_than(self):
        temp = Celsius(10)
        temp2 = Celsius(50)
        assert temp < temp2
        assert not temp2 < temp

    def test_celsius_greater_than(self):
        temp = Celsius(100)
        temp2 = Celsius(50)
        assert temp > temp2
        assert not temp2 > temp

    def test_celsius_less_or_equal(self):
        temp = Celsius(10)
        temp2 = Celsius(50)
        temp3 = Celsius(10)
        assert temp <= temp2
        assert temp <= temp3

    def test_celsius_greater_or_equal(self):
        temp = Celsius(100)
        temp2 = Celsius(50)
        temp3 = Celsius(100)
        assert temp >= temp2
        assert temp >= temp3

    def test_celsius_not_equal(self):
        temp = Celsius(10)
        temp2 = Celsius(10.1)
        assert temp != temp2


class TestCentimeterAndInch:
    def test_centimeter_equality(self):
        cm = Centimeter(20)
        cm2 = Centimeter(20)
        cm3 = Centimeter(25)
        assert cm == cm2
        assert not cm == cm3

    def test_equals_centimeter_and_inch(self):
        cm = Centimeter(20)
        inch = cm.to_inch()
        inch2 = Inch(7.874)
        assert cm == inch
        assert cm == inch2
        assert inch == inch2

    def test_centimeter_and_inch_comparisons(self):
        cm = Centimeter(12)
        cm2 = Centimeter(20)
        inch = Inch(6)
        inch2 = Inch(10)
        assert cm < cm2
        assert inch2 > inch
        assert inch < cm2
        assert inch2 > cm


class TestKilometerAndMile:
    def test_create_kilometer_and_mile(self):
        km = Kilometer(20)
        mile = Mile(20)
        assert km.value == 20
        assert mile.value == 20
        assert str(km) == "20 km"
        assert str(mile) == "20 mi."

    def test_convert_km_and_mile(self):
        km = Kilometer(20)
        mile = Mile(20)
        km2 = mile.to_kilometer()
        mile2 = km.to_mile()
        assert km == mile2
        assert mile == km2

    def test_compare_km_and_mile(self):
        km = Kilometer(20)
        km2 = Kilometer(25)
        mile = Mile(20)
        mile2 = km.to_mile()
        assert km < km2
        assert mile > km
        assert km == mile2
        assert km <= mile2
        assert km >= mile2
        assert km <= km2


class TestLiterAndGallon:
    def test_create_liter_and_gallon(self):
        liter = Liter(20)
        gallon = Gallon(20)
        assert liter.value == 20
        assert gallon.value == 20
        assert str(liter) == "20 l"
        assert str(gallon) == "20 gal"

    def test_convert_liter_and_gallon(self):
        liter = Liter(20)
        gallon = Gallon(20)
        liter2 = gallon.to_liter()
        gallon2 = liter.to_gallon()
        assert liter == gallon2
        assert gallon == liter2

    def test_compare_liter_and_gallon(self):
        liter = Liter(20)
        gallon = Gallon(20)
        liter2 = Liter(25)
        gallon2 = liter.to_gallon()
        assert liter < liter2
        assert gallon > liter
        assert liter == gallon2
        assert liter <= gallon2
        assert liter >= gallon2
        assert liter <= liter2
        assert gallon >= liter2
