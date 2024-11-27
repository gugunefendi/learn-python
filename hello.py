"""
This is multi line comment
"""

#
# these are also multi line comment
#

print("Welcome to Python App")
print("---------------------")

# Ask user for their name and age
name = input("what your name? ")
age = input("How old are you? ")

# Say hello to user
print("Hello", name, "you are", age, "years old")

""""
You can use single quote or double quote, but you should consistent
When we want print double quote inside a string, example: 'Hello "friend"'
But is better if you add backslash in string start and string end, example: 'Hello \"friend\"'
"""

# Add backslash in string start and string end
print(name, 'is my \"brother\"')

"""
F-string
Variable or expression include in string put in bracker {}
Example:
name = "Gunawan"
print(f"{name} is Amazing")
print(f"2 + 3 = {2 + 3}")
"""

print(f"{name} is Amazing")
print(f"2 + 3 = {2 + 3}")