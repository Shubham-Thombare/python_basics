# functions

#example 1 
#def happy_birthday (x, y):
#    print(f"Happy Birthday to {x}!")
#    print(f"You are {y} years old!")
#    print(f"Happy birthday to you!")
#    print()

#happy_birthday("Shubham", 18)

#example 2
#def display_invoice(username, amount, due_date):
#   print(f"Hello {username}")
#    print(f"Your bill amount of ${amount} is due on {due_date}")
#
#display_invoice("Nikhil Joshi", 1000, "01/02/2024")    

# return = statment used to end a function and send a result back to the caller
#def add(x, y):
#    z = x + y
#    return z

#print(add(1, 2))
# same can be done for other math operators
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("shubham",  "thombare")

print(full_name)
