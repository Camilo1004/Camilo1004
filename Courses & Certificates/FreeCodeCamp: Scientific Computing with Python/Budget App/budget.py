class Category:
    # Constructor
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []

    # Add an element
    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    # Take an element, as long as there is enough
    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Add the deposits and substract the withdraw to calculate how much there is
    def get_balance(self) -> float:
        return sum(i["amount"] for i in self.ledger)

    # Deposit in one category and substrack from other
    def transfer(self, amount: float, budget: "Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget.name}")
            budget.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # See if theres enough to substract or transfer
    def check_funds(self, amount: float) -> bool:
        return amount <= self.get_balance()

    def get_withdrawals(self):
        return sum(abs(item["amount"]) for item in self.ledger if item["amount"] < 0)

    def __str__(self) -> str:
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            desription = item["description"][:23]
            amount = item["amount"]
            items += f"{desription:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories: list[Category]) -> str:
    # Calculate withdrawals for each category
    withdrawals = []
    for category in categories:
        withdrawals.append(category.get_withdrawals())

    # Calculate percentages based on withdrawals
    total = sum(withdrawals)
    percentages = (
        [int((withdrawal / total) * 100) // 10 * 10 for withdrawal in withdrawals]
        if total > 0
        else [0] * len(categories)
    )

    # Create the chart header
    chart = "Percentage spent by category\n"

    # Add percentage bars
    for i in range(100, -1, -10):
        chart += f"{i:3d}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    # Add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Get the maximum name length
    max_name_length = max(len(category.name) for category in categories)

    # Add vertical category names
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            chart += category.name[i] + "  " if i < len(category.name) else "   "
        # Add newline if not the last line
        if i < max_name_length - 1:
            chart += "\n"

    return chart
