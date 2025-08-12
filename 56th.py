# Decorators (adding something without changing base function)

#(decorators)
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*you add a fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles #(decorator)   
@add_fudge 
def get_ice_cream(flavor):  #(Base func ⬇️)
    print(f"Here is your {flavor} ice cream 🍨")  #(emoji = win + ;)

get_ice_cream("Chocolate")
