def sum_of_evens(numbers):
    """
    Calculates the sum of all even numbers in a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of all even numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer values.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise TypeError("Input must be a list of integers.")
    
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum