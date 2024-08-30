# main.py
from expenses_tracker.tracker import ExpenseTracker
from expenses_tracker.utils import format_date, validate_amount
from expenses_tracker.report import generate_summary

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Generate expense summary")
        print("4. Save expenses to CSV")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            # Add a new expense
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = input("Enter the amount: ")
            description = input("Enter the description (optional): ")

            try:
                formatted_date = format_date(date)
                validated_amount = validate_amount(amount)
                tracker.add_expense(formatted_date, category, validated_amount, description)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # View all expenses
            expenses = tracker.list_expenses()
            if expenses:
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. Date: {expense.date}, Category: {expense.category}, Amount: ${expense.amount:.2f}, Description: {expense.description}")
            else:
                print("No expenses recorded.")

        elif choice == '3':
            # Generate expense summary
            summary = generate_summary(tracker.list_expenses())
            if summary:
                print("Expense Summary by Category:")
                for category, total in summary.items():
                    print(f"{category}: ${total:.2f}")
            else:
                print("No expenses recorded.")

        elif choice == '4':
            # Save expenses to CSV
            tracker.save_to_csv()
            print("Expenses saved to CSV file.")

        elif choice == '5':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 5.")

if __name__ == '__main__':
    main()
