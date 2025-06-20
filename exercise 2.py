#Exercise 2 shopping cart Program

item= input("what item would you like to buy?:")
price=float(input("what is the price?:"))
quantity=int(input("how many would you like?:"))
total=price*quantity
print(f"you have bought {quantity} x {item}/s")
print(f"your total bill amount is:${total}")