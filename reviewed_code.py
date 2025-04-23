def divide_numbers(a, b):
    """
    Divide two numbers and return the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The division result.

    Raises:
        TypeError: If either a or b is not a number.
        ZeroDivisionError: If b is zero.
    """
    # Check if both a and b are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers")

    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


# Example usage:
try:
    print(divide_numbers(10, 2))  # Should print 5.0
    print(divide_numbers(10, 0))  # Should raise ZeroDivisionError
except (TypeError, ZeroDivisionError) as e:
    print(f"Error: {e}")
