# Engine class
class Engine:
    def start(self):
        return "🚗 Engine started!"

# Car class using Engine
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Access Engine's method

# Create Engine instance
my_engine = Engine()

# Pass Engine instance to Car
my_car = Car(my_engine)

# Call Car method that uses Engine method
print(my_car.start_car())
