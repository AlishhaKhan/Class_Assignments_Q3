class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Creating object
times3 = Multiplier(3)

# Test with callable()
print("Is times3 callable?", callable(times3))  # ✅ True

# Call like a function
result = times3(10)  # Equivalent to: times3.__call__(10)
print("Result of times3(10):", result)
