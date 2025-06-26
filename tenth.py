#temperature conversion program

unit = input("Is the temperature in celsius or fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":  #(§C + 9/5)+32 = F
    temp = round((9 * temp) / 5 + 32 , 1)
    print(f"The temperature in fahrenheit is: {temp}§F")


elif unit == "F":   #(§F - 32) * 5/9 = §C
    temp = round((temp - 32) * 5/9 , 1)
    print(f"The temperature in celsius is: {temp}")

else:
    print(f"{unit} is an invalid unit of measurement")

