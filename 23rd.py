# 2D collections
# 2D list = A list made up of lists [list1 list2 list3]

fruits =     ["apple", "orange", "banana", "mango"]
vegetables = ["carrot", "potato", "bringal"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[0][1]) #(row and cloumn 0,1,2)

for collection in groceries: 
    for food in collection:
        print(food, end=" ")
        print()