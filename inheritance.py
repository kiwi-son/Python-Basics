class Animal:
    location ="India"
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal): # Dog inherits from Animal
    def speak(self):
        super().speak()  # Call the speak method of the parent class
        return "Woof! Woof!"

d=Dog("Buddy")
print(d.name)          # Output: Buddy
print(d.location)      # Output: India
print(d.speak())      # Output: Woof! Woof!