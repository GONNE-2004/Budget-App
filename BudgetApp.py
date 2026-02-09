class Category:
    def __init__(self, name):
        self.ledger = []
        # The name of the category, e.g., "Food", "Entertainment", etc.
        self.name = name

    def deposit(self, amount, description=""):
        """Deposits the specified amount into the category."""
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        """Attempts to withdraw the specified amount from the category."""
        if amount > self.check_funds(amount):  # check if there are enough funds before withdrawing
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        return True

    def get_balance(self):
        """Returns the total balance of the category."""
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        """Transfers the specified amount from this category to another category."""
        if not self.withdraw(amount, f"Transfer to {category.name}"):  # attempt to withdraw the amount from the current category with a description indicating the transfer
            return False

        # deposit the amount into the target category with a description indicating the transfer
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        """Checks if the category has enough funds for the specified amount."""
        return amount <= self.get_balance()  # check if the amount is less than or equal to the current balance

    def __str__(self):
        output = []
        # title
        output.append(self.name.center(30, "*"))
        # ledger enteries
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            output.append(f"{desc}{amount}")

        # total
        output.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(output)


def create_spend_chart(categories):
    """Creates a bar chart representing the percentage of total spending for each category."""
    pass
