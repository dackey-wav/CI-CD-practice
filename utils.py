"""Utility functions for a simple calculator."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of two numbers."""
    return a / b


def to_binary(value: int) -> str:
    """Convert a natural number from 0 to 100 into binary representation."""
    if not isinstance(value, int):
        raise TypeError("Value must be a natural number without decimal part.")

    if value < 0 or value > 100:
        raise ValueError("Value must be in range 0..100.")

    return bin(value)[2:]
