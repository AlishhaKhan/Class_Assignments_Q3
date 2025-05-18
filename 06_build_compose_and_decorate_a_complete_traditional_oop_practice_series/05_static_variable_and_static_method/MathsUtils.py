class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the static method without creating any object
print("Sum 1:", MathUtils.add(5, 3))     # Output: 8
print("Sum 2:", MathUtils.add(10, 15))   # Output: 25
