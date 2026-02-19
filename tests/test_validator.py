"""Tests for the validator module."""

from src.validator import validate_input, validate_operation, validate_divisor


class TestValidateInput:
    def test_valid_integer(self):
        valid, result = validate_input(42)     # Will FAIL: SyntaxError in validator.py
        assert valid is True
        assert result == 42.0

    def test_valid_string_number(self):
        valid, result = validate_input("3.14")
        assert valid is True
        assert result == 3.14

    def test_none(self):
        valid, msg = validate_input(None)
        assert valid is False

    def test_invalid_string(self):
        valid, msg = validate_input("hello")
        assert valid is False


class TestValidateOperation:
    def test_valid_ops(self):
        for op in ["+", "-", "*", "/"]:
            valid, result = validate_operation(op)
            assert valid is True

    def test_invalid_op(self):
        valid, msg = validate_operation("^")
        assert valid is False


class TestValidateDivisor:
    def test_nonzero(self):
        valid, result = validate_divisor(5)
        assert valid is True

    def test_zero(self):
        valid, msg = validate_divisor(0)
        assert valid is False
