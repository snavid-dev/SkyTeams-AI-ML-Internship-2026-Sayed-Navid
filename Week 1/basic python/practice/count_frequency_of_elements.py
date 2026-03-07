numbers = [3, 5, 2, 8, 1, 3, 5]

frequency = {}
for number in numbers:
  if number in frequency:
    frequency[number] += 1
  else:
    frequency[number] = 1
print("Frequency using for loop:", frequency)