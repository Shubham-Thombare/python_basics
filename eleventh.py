#logical operators (and,or,not)
# or = atleast one condition must be true 
# and = both conditions must be true
# not = inverts the conditions (not false, not true)

temp = 24
sunny = True

if temp >= 0 or temp <= 30:
 print("The temperature is good")
 print("It is sunny outside")
else:
  print("The temperature is bad")

  if  sunny:
   print("It is sunny outside")

  else:
   print("It is cloudy outside")