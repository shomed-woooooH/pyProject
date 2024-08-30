# models.py
class Expense:
    def __init__(self, date, category, amount, description=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"Expense({self.date}, {self.category}, {self.amount}, '{self.description}')"
