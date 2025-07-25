class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):

        amount = float(amount)
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        if amount > balance:
            return False
        else:
            return True

    def withdraw(self, amount, description=""):

        amount = float(amount)
        if self.check_funds(amount):
            self.ledger.append({"amount": -float(amount), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, category):

        amount = float(amount)
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        text = f"{self.name:*^30}\n"
        for item in self.ledger:
            desc = f"{item['description'][:23]}"
            amnt = f"{item['amount']:>7.2f}"
            text += f"{desc:<23}{amnt}\n"
        total = float(self.get_balance())
        text += f"Total: {total}"
        return text


def create_spend_chart(categories):
    category_data = []
    total_spend = 0
    for category in categories:
        deposit = category.ledger[0]["amount"]
        balance = category.get_balance()
        spending = deposit - balance
        total_spend += spending
        # print(f"Deposit: {deposit}, Balance: {balance}, Spending {spending}")
        category_data.append({"name": category.name, "spending": round(spending)})
    # print(f"Total Spending {total_spend}")

    # for category in category_data:
    #     # pass
    #     print(f"Percentage is {round((category['spending'] / total_spend) * 100)}")

    for i in range(100, -1, -10):
        print(f"{i:>3}|", end="")
        for category in category_data:
            percentage = (category["spending"] / total_spend) * 100
            print(" ", end="")
            if i > percentage:
                print("  ", end="")
            elif i <= percentage:
                print("o", end=" ")
        print()

    # print(category_data)
    print("    -", "-" * len(categories) * 3, sep="")

    names = [category["name"] for category in category_data]
    max_len = max(len(name) for name in names)
    padded_names = [name.ljust(max_len) for name in names]

    for i in range(max_len):
        line_letters = []
        for idx, name in enumerate(padded_names):
            letter = name[i]
            if idx == 0:
                # Add 5 spaces before the first word's letter
                line_letters.append(" " * 5 + letter)
            else:
                line_letters.append(letter)
        print("  ".join(line_letters))


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(19.99, "T-shirt")
print(food)
print(clothing)

auto = Category("Car")
auto.deposit(500, "deposit")
auto.withdraw(140, "Gas")
auto.withdraw(40, "Fix")


create_spend_chart([food, clothing, auto])
