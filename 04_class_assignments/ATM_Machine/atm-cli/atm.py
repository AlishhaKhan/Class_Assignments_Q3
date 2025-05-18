import json
import os

class ATM:
    def __init__(self, data_file='atm.json'):
        self.data_file = data_file
        self.is_authenticated = False
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.pin = data.get('pin', '1234')
                self.balance = data.get('balance', 0.0)
        else:
            self.pin = '1234'
            self.balance = 0.0
            self.save_data()

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump({
                "pin": self.pin,
                "balance": self.balance
            }, file, indent=4)

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
            print("✅ PIN verified successfully.\n")
        else:
            print("❌ Incorrect PIN. Access denied.\n")

    def check_balance(self):
        if self.is_authenticated:
            print(f"💰 Current Balance: Rs. {self.balance:.2f}\n")
        else:
            print("🔒 Please enter the correct PIN first.\n")

    def deposit(self, amount):
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                self.save_data()
                print(f"✅ Rs. {amount:.2f} deposited successfully.")
                print(f"💰 New Balance: Rs. {self.balance:.2f}\n")
            else:
                print("❌ Deposit amount must be positive.\n")
        else:
            print("🔒 Please enter the correct PIN first.\n")

    def withdraw(self, amount):
        if self.is_authenticated:
            if amount <= 0:
                print("❌ Withdrawal amount must be positive.\n")
            elif amount > self.balance:
                print("❌ Insufficient Balance.\n")
            else:
                self.balance -= amount
                self.save_data()
                print(f"✅ Rs. {amount:.2f} withdrawn successfully.")
                print(f"💰 New Balance: Rs. {self.balance:.2f}\n")
        else:
            print("🔒 Please enter the correct PIN first.\n")

    def exit(self):
        print("👋 Thank you for using the ATM. Goodbye!")
        return False

    def menu(self):
        print("==== Welcome to the ATM ====")
        attempts = 0
        while attempts < 3:
            input_pin = input("🔑 Please enter your 4-digit PIN: ")
            if input_pin == self.pin:
                self.is_authenticated = True
                print("✅ PIN verified successfully.\n")
                break
            else:
                attempts += 1
                print(f"❌ Incorrect PIN. Attempts left: {3 - attempts}\n")
        else:
            print("🚫 Too many incorrect attempts. Exiting.")
            return

        while True:
            print("==== ATM Menu ====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("➡️ Please select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("💵 Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("❌ Invalid input. Please enter a numeric value.\n")
            elif choice == "3":
                try:
                    amount = float(input("💵 Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("❌ Invalid input. Please enter a numeric value.\n")
            elif choice == "4":
                self.exit()
                break
            else:
                print("❌ Invalid selection. Please choose a valid option.\n")


if __name__ == "__main__":
    atm = ATM()
    atm.menu()
