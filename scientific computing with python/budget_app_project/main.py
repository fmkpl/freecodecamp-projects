class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
    
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}".rjust(30 - len(description))
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def check_funds(self, amount):
        balance = 0.00
        for item in self.ledger:
            balance += item['amount']
        if amount > balance:
            return False
        else:
            return True
        
    def get_balance(self):
        balance = 0.00
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, target_budget_category):
        if self.withdraw(amount, 'Transfer to ' + target_budget_category.category):
            target_budget_category.deposit(amount, 'Transfer from ' + self.category)
            return True
        return False

        
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(99, 'tax')
food.withdraw(10, 'cola')
sport = Category('Sport')
clothing = Category('Clothing')
clothing.deposit(2000)
clothing.withdraw(500, 'tax')
business = Category('Business')
business.deposit(2000)
business.withdraw(1200, 'boost')
food.transfer(500, sport)
food.transfer(200, sport)
print(food)
print(sport)

def create_spend_chart(categories):
    # Calculate total spend and percentage spend for each category
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent.append((category.category, spent))
        total_spent += spent

    percentages = [(name, int((spent / total_spent) * 100)) for name, spent in category_spent]
    percentages = [(name, (percent // 10) * 10) for name, percent in percentages]  # Round down to nearest 10

    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for name, percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"

    # Find the longest category name
    max_length = max(len(name) for name, _ in percentages)
    for i in range(max_length):
        chart += "     "
        for name, _ in percentages:
            chart += (name[i] + "  ") if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")

print(create_spend_chart([food, sport, clothing, business]))