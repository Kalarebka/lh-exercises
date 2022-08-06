import pytest

from unittest.mock import mock_open, patch

from context_manager import FileHandler


class TestFileHandler:
    @patch("builtins.open", mock_open(read_data="1,1,1,1\n2,2,2,2"))
    def test_get_lines(self):
        handler = FileHandler("test_file_name.csv")
        line = handler.get_line()
        line2 = handler.get_line()
        assert line == "1,1,1,1\n"
        assert line2 == "2,2,2,2"
