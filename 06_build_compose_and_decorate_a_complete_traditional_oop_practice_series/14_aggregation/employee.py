# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"👤 Employee Name: {self.name}"

# Department class using Aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregated Employee

    def show_details(self):
        return f"🏢 Department: {self.dept_name}\n{self.employee.get_details()}"

# Create an Employee independently
emp1 = Employee("Alice")

# Use Employee in Department (aggregation)
dept1 = Department("HR", emp1)

# Show details
print(dept1.show_details())
