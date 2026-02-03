class Category:
    def __init__(self):
        ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        if amount > self.get_balance():
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        return True

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total


def create_spend_chart(categories):
    pass
