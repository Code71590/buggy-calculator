"""
Input validation for the calculator.

Ensures that user-provided values are safe and valid
before being passed to calculator operations.
"""

def validate_input(value):         # FIXED: added missing colon
    """Validate that a value is a valid number for calculation."""
    if value is None:
        return False, "Value cannot be None"
    try:
        num = float(value)
        if num != num:  # NaN check
            return False, "Value is NaN"
        return True, num
    except (ValueError, TypeError):
        return False, f"Invalid input: {value}"


def validate_operation(op: str) -> tuple:
    """Validate that the operation string is supported."""
    valid_ops = ["+", "-", "*", "/"]
    if op in valid_ops:
        return True, op
    return False, f"Unsupported operation: '{op}'. Use one of {valid_ops}"


def validate_divisor(value: float) -> tuple:
    """Check that a divisor is not zero."""
    if value == 0:
        return False, "Division by zero is not allowed"
    return True, value
