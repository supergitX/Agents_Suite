def sum_even_numbers(numbers):
  """
  Calculates the sum of all even numbers in a list.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of all even numbers in the list. Returns 0 if the list is empty or contains no even numbers.

  Raises:
    TypeError: If the input is not a list or if the list contains non-integer values.
  """
  # Check if input is a list
  if not isinstance(numbers, list):
    raise TypeError("Input must be a list")

  # Initialize sum of even numbers to 0
  sum_of_evens = 0

  # Iterate over each number in the list
  for number in numbers:
    # Check if number is an integer
    if not isinstance(number, int):
      raise TypeError("List must contain only integers")

    # Check if number is even
    if number % 2 == 0:
      # Add even number to sum
      sum_of_evens += number

  # Return sum of even numbers
  return sum_of_evens