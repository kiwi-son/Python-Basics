class employee:
    company="HPL"

    def get_salary(self):
        return 10000
    
e=employee() #an object of employee class
print(e.get_salary()) #calling method using object
print(e.company) #accessing class variable using object


