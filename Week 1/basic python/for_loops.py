# what is for loop?
# A for loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).
# With a for loop, we can execute a block of code once for each item in the sequence.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# You can also loop through a string:
for letter in "banana":
  print(letter)

# The break statement stops the loop before it has looped through all items:
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break

# The continue statement skips the current iteration and continues with the next:
for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)

# The range() function is often used with for loops:
for number in range(6):
  print(number)  # Output: 0 to 5

# Using range(start, stop):
for number in range(2, 6):
  print(number)  # Output: 2, 3, 4, 5

# Using else in a loop:
for number in range(3):
  print(number)
else:
  print("Loop finished")

# Nested loops example:
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
  for fruit in fruits:
    print(adjective, fruit)

# The reference of this code is:
# https://www.w3schools.com/python/python_for_loops.asp

