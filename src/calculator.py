"""
Core calculator module.

Provides basic arithmetic operations: add, subtract,
multiply, divide, and square_root.
"""

from math import sqrt


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base ** exponent


def square_root(value: float) -> float:
    """Return the square root of a non-negative number.

    Raises:
        ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return sqrt(value)


def percentage(value: float, total: float) -> float:
    """Return what percentage 'value' is of 'total'."""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100


def average(*numbers: float) -> float:
    """Return the average of the given numbers."""
    if not numbers:
        raise ValueError("Need at least one number to compute average")
    return sum(numbers) / len(numbers)


def safe_multiply(a, b) -> float:
    """Multiply two values, coercing strings to numbers.

    Raises:
        TypeError: If values cannot be converted.
    """
    return a * b                   # BUG #4 (TYPE_ERROR): fails when b is a string like "3" — line 74
