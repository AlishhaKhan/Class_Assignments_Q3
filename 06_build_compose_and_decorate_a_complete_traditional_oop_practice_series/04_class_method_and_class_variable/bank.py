class Bank:
    bank_name = "ABC Bank"  # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # modifies class variable

# Creating instances
cust1 = Bank()
cust2 = Bank()

# Before change
print("Before change:")
print(cust1.bank_name)  # ABC Bank
print(cust2.bank_name)  # ABC Bank

# Changing bank name using class method
Bank.change_bank_name("SecureTrust Bank")

# After change
print("\nAfter change:")
print(cust1.bank_name)  # SecureTrust Bank
print(cust2.bank_name)  # SecureTrust Bank
