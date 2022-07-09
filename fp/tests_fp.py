import pytest

from datetime import date

from args_and_other_kwargs import list_parameters
from chunks import to_chunks
from count_days import count_days, date_from


class TestListParameters:
    def test_list_parameters_with_args_and_kwargs(self):
        result = list_parameters(42, "dog", animal="fish", other_animal="fly")
        assert len(result) == 4
        assert result[0] == 42
        assert result[1] == "dog"
        assert result["animal"] == "fish"
        

    def test_list_parameters_no_arguments(self):
        result = list_parameters()
        assert result == {}


class TestToChunks:
    def test_to_chunks_length_4_to_7(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 4, 7)
        for item in result:
            assert len(item) >= 4
            assert len(item) <= 7

    def test_to_chunks_chunk_longer_than_data(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 27, 30)
        assert len(result) == 1


class TestCountDays:
    def test_count_days_earlier_to_later_date(self):
        date1 = date(2022, 1, 1)
        date2 = date(2022, 1, 5)
        difference = count_days(date1, date2)
        assert difference == 4

    def test_count_days_later_to_earlier_date(self):
        date1 = date(2022, 1, 1)
        date2 = date(2022, 1, 5)
        difference = count_days(date2, date1)
        assert difference == 4

    def test_date_from_to_future(self):
        start_date = date(2022, 4, 1)
        result = date_from(start_date, 15)
        assert result.year == 2022
        assert result.month == 4
        assert result.day == 16

    def test_date_from_to_past(self):
        start_date = date(2022, 4, 1)
        result = date_from(start_date, -100)
        assert result.year == 2021
        assert result.month == 12
        assert result.day == 22
