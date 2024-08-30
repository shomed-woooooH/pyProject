# expenses_tracker/tracker.py

import csv
from .models import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_from_csv()  # Load expenses when the tracker is initialized

    def add_expense(self, date, category, amount, description=""):
        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)

    def list_expenses(self):
        return self.expenses

    def save_to_csv(self, filename="data/expenses.csv"):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({
                    'date': expense.date,
                    'category': expense.category,
                    'amount': expense.amount,
                    'description': expense.description
                })

    def load_from_csv(self, filename="data/expenses.csv"):
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.add_expense(
                        date=row['date'],
                        category=row['category'],
                        amount=float(row['amount']),
                        description=row['description']
                    )
        except FileNotFoundError:
            # If the file doesn't exist, we'll start with an empty list of expenses
            pass
