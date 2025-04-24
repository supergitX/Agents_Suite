def sum_of_even_numbers(numbers: list[int]) -> int:
    """
    Calculates the sum of all even numbers in a list of integers.

    Args:
      numbers: A list of integers.

    Returns:
      The sum of all even numbers in the list.

    Raises:
      TypeError: If the input is not a list or if the list contains non-integer values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    sum_even = 0
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("All elements in the list must be integers.")
        if number % 2 == 0:
            sum_even += number
    return sum_even