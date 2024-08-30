# utils.py
from datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

def validate_amount(amount_str):
    try:
        return float(amount_str)
    except ValueError:
        raise ValueError("Invalid amount")
