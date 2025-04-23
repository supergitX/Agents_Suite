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
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    print(divide_numbers(10, 0))
except ValueError as e:
    print(e)