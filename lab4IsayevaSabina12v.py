def lazy_filter(sequence, condition):
  return filter(condition, sequence)


def read_numbers_from_input():
  input_numbers = input("числа через пробел ").split()
  numbers = map(int, input_numbers)
  return numbers


numbers = read_numbers_from_input()
even_numbers = lazy_filter(numbers, lambda x: x % 2 == 0)
print("четные числа ", list(even_numbers))
numbers_greater_than_5 = lazy_filter(numbers, lambda x: x > 5)
print("больше 5 ", list(numbers_greater_than_5))
