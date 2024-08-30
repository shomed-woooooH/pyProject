# test_tracker.py
import unittest
from expenses_tracker.tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense('2024-08-30', 'Groceries', 50.0)
        self.assertEqual(len(self.tracker.list_expenses()), 1)

    def test_delete_expense(self):
        self.tracker.add_expense('2024-08-30', 'Groceries', 50.0)
        self.tracker.delete_expense(0)
        self.assertEqual(len(self.tracker.list_expenses()), 0)

if __name__ == '__main__':
    unittest.main()
