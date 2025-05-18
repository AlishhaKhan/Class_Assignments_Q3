class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"🐾 {self.name} says: Woof woof!")

# Create an object of Dog
my_dog = Dog("Roger", "Husky")

# Call the instance method
my_dog.bark()
