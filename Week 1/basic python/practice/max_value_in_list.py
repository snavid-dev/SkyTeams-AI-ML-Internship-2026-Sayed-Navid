numbers = [3, 5, 2, 8, 1]

# first option to find the max value in the list
max_value = max(numbers)
print("Max value using max() function:", max_value)

# second option to find the max value in the list
for index, value in enumerate(numbers):
  if index == 0:
    max_value = value
  elif value > max_value:
    max_value = value
print("Max value using for loop:", max_value)