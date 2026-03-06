fruits = ["apple", "banana", "cherry"]

fruits.append("mango")
fruits.remove("apple")
print(fruits[0])  # the first item
print(fruits[-1])  # the last item
print(fruits[1:3])  # from index 1 to index 2 (not including index 3)
print(fruits[::2])  # every second item
fruits.sort()  # sorts the list in place
fruits.reverse()  # reverses the list in place
print(fruits)
