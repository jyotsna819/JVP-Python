from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Lambda with map
squares = list(map(lambda x: x * x, numbers))

# Reduce to sum
sum_result = reduce(lambda a, b: a + b, numbers)

# Optional-like check
first_even = next((x for x in numbers if x % 2 == 0), None)

# Output
print("Evens:", evens)
print("Squares:", squares)
print("Sum:", sum_result)
print("First Even:", first_even if first_even is not None else -1)
