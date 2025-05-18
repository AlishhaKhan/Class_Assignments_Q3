# student.py

class Student:
    def __init__(self, name, marks):
        self.name = name          # using self to initialize name
        self.marks = marks        # using self to initialize marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Sample usage
student1 = Student("Alisha", 92)
student1.display()
