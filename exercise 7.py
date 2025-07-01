# validate user input exercise (thirtenth)

# Username is no more than 12 characters
# Username must not contain spaces
# Username must not contain digits

username = input("Enter the username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces ")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")