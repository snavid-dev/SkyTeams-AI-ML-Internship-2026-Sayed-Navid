# what is function?
# A function is a block of code that only runs when it is called.
# You can pass data (parameters) into a function, and a function can return data as a result.

def myFunction():
  print("Hello from a function")

myFunction()

# Information can be passed into functions as arguments:
def myFunctionWithName(name):
  print(name + " Refsnes")

myFunctionWithName("Emil")
myFunctionWithName("Tobias")
myFunctionWithName("Linus")

# Number of arguments matters:
def myFunctionWithTwoNames(firstName, lastName):
  print(firstName + " " + lastName)

myFunctionWithTwoNames("Emil", "Refsnes")

# Arbitrary arguments, *args:
def myKids(*kids):
  print("The youngest child is " + kids[2])

myKids("Emil", "Tobias", "Linus")

# Keyword arguments:
def myChild(child3, child2, child1):
  print("The youngest child is " + child3)

myChild(child1="Emil", child2="Tobias", child3="Linus")

# Default parameter value:
def myCountry(country="Norway"):
  print("I am from " + country)

myCountry("Sweden")
myCountry("India")
myCountry()
myCountry("Brazil")

# Return values:
def multiplyByFive(number):
  return 5 * number

print(multiplyByFive(3))
print(multiplyByFive(5))
print(multiplyByFive(9))

# The reference of this code is:
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_functions_arguments.asp

