import math   #(formula to calc hypotenuse of right angled tri, fifth) 
a= float(input("Enter side A: "))
b= float(input("Enter side B: "))

c= math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side C ={c}")