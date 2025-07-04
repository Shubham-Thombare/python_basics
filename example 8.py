#while loops
# exercise (Example)

#food = input("Enter a food you like (q to quit): ")
 
#while not food == "q":
 #print(f"you like {food}") 
 #food = input("Enter another food you like (q to quit): ")

#print("bye")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = (input("Enter your age: "))

print(f"You are {age} years old")