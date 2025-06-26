# Python weight converter

weight = float(input("Enter a weight: "))
unit = input("kilogram or Pounds? (K or L): ")

if unit == "K":
 weight = weight * 2.205
 unit = "Lbs."
 print(f"Your weight is: {round(weight,2)} {unit}") 

 
elif unit == "L":
 weight = weight / 2.205
 unit = "Kgs"
 print(f"Your weight is: {round(weight,2)} {unit}")

    
else:
 print(f"{unit} is not valid")


