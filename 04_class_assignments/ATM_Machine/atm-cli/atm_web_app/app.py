from flask import Flask, render_template, request
from atm import ATM

app = Flask(__name__)
atm = ATM()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    balance = None

    if request.method == "POST":
        action = request.form.get("action")
        pin = request.form.get("pin")
        amount = request.form.get("amount")

        if not atm.is_authenticated:
            atm.check_pin(pin)
            message = "✅ PIN verified." if atm.is_authenticated else "❌ Incorrect PIN."

        if atm.is_authenticated:
            if action == "deposit":
                atm.deposit(float(amount))
                message = f"✅ Deposited Rs. {amount}"
            elif action == "withdraw":
                atm.withdraw(float(amount))
                message = f"✅ Withdrawn Rs. {amount}"
            balance = atm.balance

    return render_template("index.html", message=message, balance=balance)

if __name__ == "__main__":
    app.run(debug=True)
