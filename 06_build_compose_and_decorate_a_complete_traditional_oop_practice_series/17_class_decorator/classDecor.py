# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create object and call new method
p = Person("Alisha")
print(p.greet())  # Output: Hello from Decorator!
