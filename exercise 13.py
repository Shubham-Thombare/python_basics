# list compherensions
# formula = [expressiom for value in iterable if condition]

# for expression
fruits = ["apple", "banana", "coconut", "mango"]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruit_chars)

# for if condition
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(odd_nums)

# list of grades
grades = [85, 45, 76, 89,20, 95]
passing_grades = [grade for grade in grades if grade >= 80]

print(passing_grades)