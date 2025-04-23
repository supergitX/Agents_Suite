def sum_even_numbers(numbers):
  """
  Calculates the sum of all even numbers in a list of integers.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of all even numbers in the list.

  Raises:
    TypeError: If the input list is None or contains non-integer values.
    ValueError: If the input list is empty.
  """
  if numbers is None:
    raise TypeError("Input list cannot be None")
  if not numbers:
    raise ValueError("Input list cannot be empty")
  
  try:
    sum_of_evens = sum(num for num in numbers if isinstance(num, int) and num % 2 == 0)
  except TypeError:
    raise TypeError("Input list must only contain integers")
  
  return sum_of_evens