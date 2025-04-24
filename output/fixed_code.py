def calculate_sum_of_even_numbers(numbers: list[int]) -> int:
  """
  Calculates the sum of all even numbers in a list.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of all even numbers in the list. If the list is empty or contains no even numbers, returns 0.
  """
  if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
    raise ValueError("Input must be a list of integers")
  
  sum_of_even_numbers = 0
  for number in numbers:
    if number % 2 == 0:
      sum_of_even_numbers += number
  return sum_of_even_numbers