def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in a list of integers.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    sum_of_evens = 0
    for number in numbers:
        if number % 2 == 0:
            sum_of_evens += number
    return sum_of_evens