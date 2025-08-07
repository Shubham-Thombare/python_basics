# Static Method

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod 
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "janitor"]
        return position in valid_positions
    
employee1 = Employee("Harry", "Manager")
employee2 = Employee("petter", "Cashier")
employee3 = Employee("Max", "Cook")   
    
print(Employee.is_valid_position("Manager"))   
    
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
