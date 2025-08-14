# writing files (.txt, .json, .csv) (.csv = common seperated values)

# employees = ["Eugene", "James", "George", "Ellie"]

#file_path = "C:/Users/HP/OneDrive/Desktop/output.txt" 

#try:
#    with open(file_path, "a") as file:
#        for employee in employees:
#            file.write("\n" + employee)
#        print(f"txt file '{file_path}' created successfully.")
#except FileExistsError:
#    print(f"txt file '{file_path}' already exists.")


#import json

#employee = {
#    "name": "Robert",
#    "age": "24",
#    "job": "writer"
#}

#file_path = "C:/Users/HP/OneDrive/Desktop/output.json" 

#try:
#    with open(file_path, "w") as file:
#        json.dump(employee, file, indent=4)
#        print(f"json file '{file_path}' created successfully.")
#except FileExistsError:
#    print(f"txt file '{file_path}' already exists.")



import json
import csv

employees = [["Name", "Age", "Job"],
            ["James", 30, "Cook"],
            ["Ellie", 27, "Unemployed"],
            ["Sweety", 24, "Scientist"]]

file_path = "C:/Users/HP/OneDrive/Desktop/output.csv" 

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' created successfully.")
except FileExistsError:
    print(f"txt file '{file_path}' already exists.")
