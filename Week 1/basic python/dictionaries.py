# what is dictionary?
# A dictionary is a collection of key-value pairs in Python. It is an unordered, mutable, and indexed data structure that allows you to store and retrieve values based on unique keys. Each key in a dictionary must be unique, and it is used to access the corresponding value. Dictionaries are defined using curly braces {} and the key-value pairs are separated by colons (:). For example:


thisDictionary = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# In this example, "name", "age", and "city" are the keys, and "John", 30, and "New York" are the corresponding values. You can access the values in a dictionary using their keys. For instance, to access the value associated with the key "name", you can use:
print(thisDictionary["name"])  # Output: John

# You can also add new key-value pairs to a dictionary or update existing ones. For example:
thisDictionary["email"] = "info@email.com"

print(thisDictionary)

# dictionaries also have various methods for manipulating and accessing data, such as keys(), values(), items(), get(), and more. For example, to get a list of all the keys in the dictionary, you can use:
print(thisDictionary.keys())  # Output: dict_keys(['name', 'age', 'city', 'email'])

# To get a list of all the values in the dictionary, you can use:
print(thisDictionary.values())  # Output: dict_values(['John', 30, 'New York', 'info@email.com'])

# how to get the length of dictionaries
print(len(thisDictionary))  # Output: 4

# the type of dictionaries are objects 🫨
print(type(thisDictionary))  # Output: <class 'dict'>

# dict() is a built-in function in Python that is used to create a new dictionary. It can be used in several ways to create dictionaries:
# 1. Using curly braces {}:
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}

# 2. Using the dict() constructor with keyword arguments:
my_dict = dict(key1="value1", key2="value2")
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}

# also we have lists and tuples


# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# The reference of this code is: https://www.w3schools.com/python/python_dictionaries.asp
