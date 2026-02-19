"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide, power, average, safe_multiply


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_numbers(self):
        assert add(-1, 1) == 0

    def test_floats(self):
        assert round(add(0.1, 0.2), 10) == round(0.3, 10)


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2          # Will FAIL due to LOGIC bug

    def test_negative_result(self):
        assert subtract(3, 5) == -2         # Will FAIL due to LOGIC bug

    def test_same_numbers(self):
        assert subtract(7, 7) == 0          # Will FAIL due to LOGIC bug


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0

    def test_float_division(self):
        assert round(divide(1, 3), 4) == 0.3333

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(1, 0)


class TestPower:
    def test_square(self):
        assert power(3, 2) == 9

    def test_zero_exponent(self):
        assert power(5, 0) == 1


class TestAverage:
    def test_integers(self):
        assert average(2, 4, 6) == 4.0

    def test_single_value(self):
        assert average(10) == 10.0

    def test_empty(self):
        with pytest.raises(ValueError):
            average()


class TestSafeMultiply:
    def test_integers(self):
        assert safe_multiply(3, 4) == 12

    def test_string_number(self):
        assert safe_multiply(5, "3") == 15   # Will FAIL due to TYPE_ERROR bug
