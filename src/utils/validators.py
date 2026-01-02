"""
Validation utilities for the Console Todo Application.
"""


def validate_todo_title(title: str) -> bool:
    """
    Validate that a todo title is not empty or whitespace-only.

    Args:
        title: The title to validate

    Returns:
        True if the title is valid, False otherwise
    """
    if not title:
        return False
    if not title.strip():
        return False
    return True


def validate_todo_id(todo_id: str) -> bool:
    """
    Validate that a todo ID is a positive integer string.

    Args:
        todo_id: The ID string to validate

    Returns:
        True if the ID is valid, False otherwise
    """
    if not todo_id:
        return False
    if not todo_id.strip():
        return False
    try:
        id_int = int(todo_id.strip())
        return id_int > 0
    except ValueError:
        return False


def is_valid_status(status: str) -> bool:
    """
    Validate that a status is one of the allowed values.

    Args:
        status: The status to validate

    Returns:
        True if the status is valid, False otherwise
    """
    return status.lower() in ["pending", "complete"]