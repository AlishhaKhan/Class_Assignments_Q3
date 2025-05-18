class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):
        print(f"{self.brand} car is starting...")  # public method

# Instantiate the class
my_car = Car("Toyota")

# Access public variable and method from outside
print(my_car.brand)      # Output: Toyota
my_car.start()           # Output: Toyota car is starting...
