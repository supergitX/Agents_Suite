def divide_numbers(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The division result if b is not zero, otherwise None.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

try:
    print(divide_numbers(10, 0))
except ValueError as e:
    print(f"Error: {e}")

# Example usage with valid input
print(divide_numbers(10, 2))