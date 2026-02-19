"""
Utility functions for the calculator.

Provides formatting helpers and common operations
used throughout the calculator package.
"""

import sys
import json
import re
import logging
from typing import Optional
from datetime import datetime
import os                          # BUG #1 (LINTING): unused import 'os' — line 15


logger = logging.getLogger(__name__)


def format_result(operation: str, a: float, b: float, result: float) -> str:
    """Format a calculation result as a human-readable string."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {a} {operation} {b} = {result}"


def parse_number(value: str) -> Optional[float]:
    """Parse a string into a number, returning None if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        logger.warning(f"Could not parse '{value}' as a number")
        return None


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max bounds."""
    return max(min_val, min(value, max_val))


def is_close(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """Check if two floats are approximately equal."""
    return abs(a - b) < tolerance
