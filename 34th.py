# Iterables
#list and tuple both are iterables

numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number, end=" ")

# for set:
#set are reversible but reversed(order) is not allowed.

fruits = {"apple", "banana", "mango", "orange"}    

for fruit in fruits:
    print(fruit)

# string
name = "Shubham Thombare"

for character in name:
    print(character, end=" ")

# dictionary
my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")