class employee:
    def __init__(self, salary, name, bond):
        self.salary=salary #create an instance attribute 
        self.name=name 
        self.bond=bond
    def get_salary(self):
        return self.salary
    def get_info(self):
        return f"name is {self.name}. Bond period is {self.bond} years."


e1=employee(10000,"Harry",2) #object creation with parameters
print(e1.get_salary()) #calling method using object
print(e1.get_info())