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
        if not self.check_funds(amount):  # check if there are enough funds before withdrawing
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
        # center the category name within a width of 30 characters, using "*" as the fill character on both sides
        output.append(self.name.center(30, "*"))
        # ledger enteries
        for item in self.ledger:
            # take the first 23 characters of the description and left-align it within a width of 23 characters
            desc = item["description"][:23].ljust(23)
            # format the amount to 2 decimal places and right-align it within a width of 7 characters
            amount = f"{item['amount']:.2f}".rjust(7)
            output.append(f"{desc}{amount}")

        # total
        output.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(output)


def create_spend_chart(categories):
    """Creates a bar chart representing the percentage of total spending for each category."""

    # Calculate total spending for each category and overall total spending
    category_spent = []
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            amt = item["amount"]
            if amt < 0:  # only consider negative amounts as spending
                spent += -amt
        category_spent.append(spent)
    total_spent = sum(category_spent)

    # Calculate percentage spent for each category
    percents = []
    for spent in category_spent:
        # calculate the percentage and convert to an integer
        percent = int((spent / total_spent) * 100) // 10 * 10
        # int truncates the percentage to the nearest lower multiple of 10
        percents.append(percent)

    # Create the bar chart
    lines = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        # format the percentage label to be right-aligned within a width of 3 characters, followed by a vertical bar
        line = f"{i:>3}|"
        for p in percents:
            # add " o " if the percentage is greater than or equal to the current level, otherwise add spaces
            line += " o " if p >= i else "   "
        line += " "  # add a space at the end of the line for formatting
        lines.append(line)
