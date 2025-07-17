# count up timer (default arguments)
import time

def count(end, start = 0):  
 #(start = 0 is non default argument and as of default argument, non default argument should follows default argument : reason for taking start = 0 in right hand side)
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!!")
              
count(25, 15)              
