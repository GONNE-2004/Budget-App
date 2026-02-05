class Category:
    def __init__(self):
        self.ledger = []

    def deposit(self, amount, description=""):
        """Deposits the specified amount into the category."""
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        """Attempts to withdraw the specified amount from the category."""
        if amount > self.get_balance():
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
        if not self.withdraw(amount, f"Transfer to {category.name}"):
            return False

        category.deposit(amount, f"Transfer from {self.name}")
        return True


def create_spend_chart(categories):
    pass
