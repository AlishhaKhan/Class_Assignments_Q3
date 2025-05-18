class A:
    def show(self):
        print("A: show() method")

class B(A):
    def show(self):
        print("B: show() method")

class C(A):
    def show(self):
        print("C: show() method")

class D(B, C):  # Diamond inheritance
    pass

# Create object of D
d = D()

# Call the show() method
d.show()

# Check Method Resolution Order
print("MRO of class D:", D.__mro__)
