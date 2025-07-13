# dictionaries

capitals = {"India": "New Delhi",
           "USA": "Washington D.C.",
           "Russia": "Moscow",
           "China":"Beijing"}

# print(dir(capitals))
# print(help(capitals))

#print(capitals.get("China"))

#if capitals.get("China"):
#   print("That capital exists")
#else:
#   print("That capital doesn't exist")

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("Russia")
#capitals.popitem()    #(popitem: to remove latest key:value (the last entered))
#capitals.clear()

#keys= capitals.keys() 

#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(values)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
