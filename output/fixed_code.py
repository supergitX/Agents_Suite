def sum_even_numbers(numbers: list[int]) -> int:
    """
    Calculate the sum of all even numbers in a list of integers.

    Args:
      numbers: A list of integers.

    Returns:
      The sum of all even numbers in the list.

    Raises:
      TypeError: If the input is not a list or if the list contains non-integer values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers")

    sum_of_evens = 0
    for number in numbers:
        if number % 2 == 0:
            sum_of_evens += number
    return sum_of_evens