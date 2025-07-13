from reviewed_code import factorial
import pytest

def test_factorial_valid_inputs():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(5) == 120

def test_factorial_invalid_inputs():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-5)
    with pytest.raises(ValueError):
        factorial(-10)

def test_factorial_non_integer_inputs():
    with pytest.raises(ValueError):
        factorial(3.5)
    with pytest.raises(ValueError):
        factorial(2.0)
    with pytest.raises(ValueError):
        factorial("5")

def test_factorial_none_input():
    with pytest.raises(ValueError):
        factorial(None)

def test_factorial_empty_string_input():
    with pytest.raises(ValueError):
        factorial("")

def test_factorial_large_input():
    assert factorial(20) == 2432902008176640000

def test_factorial_invalid_type_input():
    with pytest.raises(ValueError):
        factorial([5])
    with pytest.raises(ValueError):
        factorial({"a": 5})
    with pytest.raises(ValueError):
        factorial((5,))

def test_factorial_float_input():
    with pytest.raises(ValueError):
        factorial(5.0)

def test_factorial_complex_input():
    with pytest.raises(ValueError):
        factorial(5 + 3j)