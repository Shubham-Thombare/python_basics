# args and kwargs
#*args - arguments
#**kwargs - keyword arguments

#args:
#example 1
def add(*args):   #(instead of args i can use any different  name with astertick)
    total = 0
    for arg in args:
        total += arg
    return total
    
print(add(1, 2, 3))    

#example 2
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.", "Shubham", "Thombare")        


#kwargs:
#example 1
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123",
              city="pune",
              state="maharashtra",
              zip= "411043")    
