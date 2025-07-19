# membership operators

#example 1
word = "APPLE"

letter = input(f"Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} ")
else:
    print(f"{letter} was not found")


#example 2
students = {"Shubham", "Nikhil", "Omkar"}

student = input("Enter the name of student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")   

# example 3
grades =  {"Sandy": "A",
           "Patrick": "B",
           "Roman": "C",
           "Eley": "D"}    
student = input("Enter the name of student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

# example 4
email = "shubham12gmail.com"    

if "@" in email and "." in email:
    print(f"Valid email")
else:
    print(f"Invalid email")    