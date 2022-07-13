import pytest

from measurements import Celsius, Fahrenheit

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

    
