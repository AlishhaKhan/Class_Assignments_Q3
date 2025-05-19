class Student:
    def __init__(self, name, marks):
        self.name = name        # 'self' refers to the current object
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Test the class
student1 = Student("Alisha", 92)
student1.display()
