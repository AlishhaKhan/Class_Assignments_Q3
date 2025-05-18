# counter.py

class Counter:
    count = 0  # Class variable to keep track of instances

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Sample usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
