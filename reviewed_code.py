def sum_of_evens(numbers: list[int]) -> int:
    """
    Calculate the sum of all even numbers in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.

    Raises:
        TypeError: If the input is not a list or if the list contains non-integer values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers")

    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
    return sum_even