class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            print("Setting price...")
            self._price = value
        else:
            print("❌ Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Usage
item = Product(500)
print(item.price)     # Access with @property

item.price = 800      # Update with @setter
print(item.price)

item.price = -100     # Invalid update

del item.price        # Delete with @deleter
