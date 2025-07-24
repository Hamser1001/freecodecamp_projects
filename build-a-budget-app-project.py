class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        try:
            amount = float(amount)
            self.ledger.append({"amount": amount, "description": description})
        except ValueError:
            print("Amount is a real number")

    def check_funds(self, amount):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        if amount > balance:
            return False
        else:
            return True

    def withdraw(self, amount, description=""):
        try:
            if self.check_funds(amount):
                self.ledger.append(
                    {"amount": -float(amount), "description": description}
                )
                return True
            else:
                return False
        except ValueError:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance


def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(200, "Groceries")
print(food.get_balance())