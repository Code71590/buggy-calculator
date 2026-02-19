"""Tests for the utils module."""

from src.utils import format_result, parse_number, clamp, is_close


class TestFormatResult:
    def test_addition(self):
        result = format_result("+", 2, 3, 5)
        assert "2 + 3 = 5" in result

    def test_contains_timestamp(self):
        result = format_result("*", 4, 5, 20)
        assert "[" in result and "]" in result


class TestParseNumber:
    def test_integer_string(self):
        assert parse_number("42") == 42.0

    def test_float_string(self):
        assert parse_number("3.14") == 3.14

    def test_invalid_string(self):
        assert parse_number("abc") is None

    def test_none(self):
        assert parse_number(None) is None


class TestClamp:
    def test_within_bounds(self):
        assert clamp(5, 0, 10) == 5

    def test_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_above_max(self):
        assert clamp(15, 0, 10) == 10


class TestIsClose:
    def test_equal_floats(self):
        assert is_close(1.0, 1.0) is True

    def test_close_floats(self):
        assert is_close(0.1 + 0.2, 0.3) is True

    def test_different_floats(self):
        assert is_close(1.0, 2.0) is False
