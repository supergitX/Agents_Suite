def divide_numbers(a, b):
    """
    Divide two numbers and return the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The division result.

    Raises:
        ZeroDivisionError: If the divisor is zero.
        TypeError: If either input is not a number.
    """
    # Check if inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")

    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Perform division
    return a / b

# Example usage:
try:
    result = divide_numbers(10, 2)
    print(result)
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")

# Test with invalid input
try:
    result = divide_numbers(10, 0)
    print(result)
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")