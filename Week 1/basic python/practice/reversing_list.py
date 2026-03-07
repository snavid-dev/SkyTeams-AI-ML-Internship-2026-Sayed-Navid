fruits = ["apple", "banana", "orange"]

# first option to reverse the list
print(fruits)
# reversing the list
fruits = fruits[::-1]
print(fruits)

# second option to reverse the list
print(fruits)
# reversing the list
fruits.reverse()
print(fruits)

# third option to reverse the list
print(fruits)
# reversing the list
fruits = list(reversed(fruits))
print(fruits)

# fourth option to reverse the list
print(fruits)
# reversing the list
fruits.sort(reverse=True)
print(fruits)

# fifth option to reverse the list
reversed_fruits = []
for index, fruit in enumerate(reversed(list(fruits))):
  reversed_fruits.append(fruit)
print(reversed_fruits)

# there are many more ways to reverse a list, but these are some of the most common ones.


