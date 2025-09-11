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
        text += f"Total: {total:.2f}"
        return text


def create_spend_chart(categories):
    spendings = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spendings.append(spent)
    
    total_spent = sum(spendings)
    
    percentages = []
    for spending in spendings:
        if total_spent == 0:
            percent = 0
        else:
            percent = spending / total_spent * 100
            percent = (percent // 10) * 10  
        percentages.append(percent)
    
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_length = max(len(category.name) for category in categories)
    
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
    
    return chart


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


print(create_spend_chart([food, clothing, auto]))
print(create_spend_chart([food, clothing]))