class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

emp1 = Employee("Alisha", 60000, "123-45-6789")

# Accessing public variable
print("✅ Public Name:", emp1.name)

# Accessing protected variable (works, but use with caution)
print("🟡 Protected Salary:", emp1._salary)

# Accessing private variable directly (will fail)
try:
    print("❌ Private SSN:", emp1.__ssn)
except AttributeError:
    print("❌ Cannot access private variable '__ssn' directly.")

# Accessing private variable via name mangling (works)
print("🔓 Private SSN (via mangling):", emp1._Employee__ssn) # type: ignore
