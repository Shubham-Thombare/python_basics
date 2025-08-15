# reading files

#file_path = "C:/Users/HP/OneDrive/Desktop/output.txt"

#try:
#    with open(file_path, "r") as file:
#        content = file.read()
#        print(content)
#except FileNotFoundError:  
#    print("That file was not found")
#except PermissionError:
#    print("You don't have permission to read that file")



#import json

#file_path = "C:/Users/HP/OneDrive/Desktop/output.json"

#try:
#    with open(file_path, "r") as file:
#        content = json.load(file)
#        print(content["name"])
#except FileNotFoundError:  
#    print("That file was not found")
#except PermissionError:
#    print("You don't have permission to read that file")



import csv

file_path = "C:/Users/HP/OneDrive/Desktop/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:  
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")