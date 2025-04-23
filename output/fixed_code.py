def divide_numbers(a, b):
    """
    Divide two numbers and handle potential division by zero error.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")