"""Unit tests for calculator utility functions."""

import pytest

import utils


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)],
)
def test_add(a: int, b: int, expected: int) -> None:
    """Test integer addition."""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)],
)
def test_subtract(a: int, b: int, expected: int) -> None:
    """Test integer subtraction."""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)],
)
def test_multiply(a: int, b: int, expected: int) -> None:
    """Test integer multiplication."""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)],
)
def test_divide(a: int, b: int, expected: float) -> None:
    """Test division results."""
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "value,expected",
    [(0, "0"), (1, "1"), (2, "10"), (10, "1010"), (100, "1100100")],
)
def test_to_binary_valid_range(value: int, expected: str) -> None:
    """Test binary conversion for valid natural numbers."""
    result = utils.to_binary(value)
    assert result == expected


@pytest.mark.parametrize("value", [-1, 101])
def test_to_binary_out_of_range(value: int) -> None:
    """Test binary conversion fails for values outside 0..100."""
    with pytest.raises(ValueError):
        utils.to_binary(value)


@pytest.mark.parametrize("value", [3.5, -0.1, 10.0])
def test_to_binary_non_natural_number(value: float) -> None:
    """Test binary conversion fails for non-integer numbers."""
    with pytest.raises(TypeError):
        utils.to_binary(value)
