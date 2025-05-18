# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the constructor of the base class
        self.subject = subject
        print(f"Teacher initialized: {self.name} teaches {self.subject}")

# Create object
t1 = Teacher("Alisha", "Python Programming")
