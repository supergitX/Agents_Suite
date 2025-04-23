def divide_numbers(a, b):
    """
    Divide two numbers and return the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        TypeError: If a or b is not a number.
        ZeroDivisionError: If b is zero.
    """
    # Validate input values
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers")

    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Perform division
    return a / b

try:
    print(divide_numbers(10, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")