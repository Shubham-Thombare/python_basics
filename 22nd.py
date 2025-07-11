# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the foood you want to buy (q to quit): ")   #("to enable while loop q function is used")
    if food.lower() == "q":      #(.lower is used to temporarily make user input lowercase)
        break
    else:
       price = float(input(f"Enter the price of a {food}: $"))
       foods.append(food)
       prices.append(price)
       #(if-else statment should lie in one line ("be careful"))

print("-----Your Cart-----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")
