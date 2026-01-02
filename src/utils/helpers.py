"""
Helper utilities for the Console Todo Application.
"""
from datetime import datetime
from typing import Optional


def format_timestamp(timestamp: Optional[datetime]) -> str:
    """
    Format a datetime object to a readable string.

    Args:
        timestamp: The datetime to format

    Returns:
        Formatted timestamp string or "N/A" if None
    """
    if timestamp is None:
        return "N/A"
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def format_status(status: str) -> str:
    """
    Format a status string for display.

    Args:
        status: The status to format

    Returns:
        Formatted status string
    """
    return status.upper()


def generate_id(start_id: int = 1) -> int:
    """
    Generate a unique ID starting from a given value.

    Args:
        start_id: The starting ID value

    Returns:
        The generated ID
    """
    return start_id


def is_positive_integer(value: int) -> bool:
    """
    Check if a value is a positive integer.

    Args:
        value: The value to check

    Returns:
        True if the value is a positive integer, False otherwise
    """
    return isinstance(value, int) and value > 0