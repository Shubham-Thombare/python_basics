# shipping_label (*args and **kwargs)

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()    

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "Pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('Pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('zip')} {kwargs.get('state')}") 

shipping_label("Mr.", "Shubham", "Thomobare",
               street= "123",
               apt= "#100",
               Pobox= "PO BOX 145",
               city= "pune",
               zip= "41104",
               state= "maharashtra",)
               
                   