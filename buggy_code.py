def sum_of_evens(numbers):
    """
    Calculate the sum of all even numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
    return sum_even