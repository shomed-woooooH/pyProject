# report.py
from collections import defaultdict

def generate_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return dict(summary)
