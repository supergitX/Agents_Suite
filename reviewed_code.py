# corrected_code.py

def divide_numbers(a, b):
    """
    Divides two numbers and returns the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The division result.

    Raises:
        ZeroDivisionError: If the divisor is 0.
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    print("Result:", divide_numbers(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)

# Example usage
try:
    print("Result:", divide_numbers(10, 2))
except Exception as e:
    print("An error occurred:", e)