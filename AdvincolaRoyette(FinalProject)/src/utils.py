"""
utils.py

Utility helper functions.
"""


def validate_number(value):
    """
    Validates numeric input.
    """
    try:
        return float(value)
    except ValueError:
        return None