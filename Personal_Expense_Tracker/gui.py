import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from expenses_tracker.tracker import ExpenseTracker
from expenses_tracker.utils import validate_amount
from expenses_tracker.report import generate_summary

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")

        self.tracker = ExpenseTracker()

        # Set up styles
        self.setup_styles()

        # Create widgets
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white", padding=10)
        style.map("TButton", background=[('active', '#45a049')])
        style.configure("TEntry", font=("Arial", 12), padding=5)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    def create_widgets(self):
        # Date Entry with Calendar
        ttk.Label(self.root, text="Date:").grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.date_entry.bind("<Return>", lambda e: self.focus_next_widget(self.category_entry))

        # Other Entries for Category, Amount, and Description
        ttk.Label(self.root, text="Category:").grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = ttk.Entry(self.root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)
        self.category_entry.bind("<Return>", lambda e: self.focus_next_widget(self.amount_entry))

        ttk.Label(self.root, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.amount_entry.bind("<Return>", lambda e: self.focus_next_widget(self.description_entry))

        ttk.Label(self.root, text="Description (optional):").grid(row=3, column=0, padx=10, pady=10)
        self.description_entry = ttk.Entry(self.root)
        self.description_entry.grid(row=3, column=1, padx=10, pady=10)
        self.description_entry.bind("<Return>", lambda e: self.add_expense())

        # Buttons for Add, View, Summary, Save, and Exit
        ttk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="View Expenses", command=self.view_expenses).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Generate Summary", command=self.generate_summary).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Save to CSV", command=self.save_to_csv).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).grid(row=8, column=0, columnspan=2, pady=10)

        # Treeview widget for displaying expenses in a table
        self.expense_table = ttk.Treeview(self.root, columns=("Date", "Category", "Amount", "Description"), show='headings')
        self.expense_table.heading("Date", text="Date")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Amount", text="Amount")
        self.expense_table.heading("Description", text="Description")

        # Set column widths
        self.expense_table.column("Date", width=100)
        self.expense_table.column("Category", width=100)
        self.expense_table.column("Amount", width=100)
        self.expense_table.column("Description", width=200)

        self.expense_table.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Make the table widget expand when the window is resized
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def focus_next_widget(self, widget):
        widget.focus_set()

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        try:
            validated_amount = validate_amount(amount)
            self.tracker.add_expense(date, category, validated_amount, description)
            self.tracker.save_to_csv()  # Automatically save to CSV after adding
            messagebox.showinfo("Success", "Expense added and saved successfully.")
            self.clear_entries()
            self.update_table()  # Update the table with the new expense
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def view_expenses(self):
        self.update_table()  # Update the table whenever "View Expenses" is clicked

    def generate_summary(self):
        summary = generate_summary(self.tracker.list_expenses())
        if summary:
            summary_list = "\n".join([f"{cat}: ${total:.2f}" for cat, total in summary.items()])
            messagebox.showinfo("Summary", summary_list)
        else:
            messagebox.showinfo("Summary", "No expenses recorded.")

    def save_to_csv(self):
        self.tracker.save_to_csv()
        messagebox.showinfo("Saved", "Expenses saved to CSV file.")

    def clear_entries(self):
        # Clear the Category, Amount, and Description entries, but keep the date as the selected date
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.focus_set()  # Set focus back to the date entry

    def update_table(self):
        # Clear the current table
        for row in self.expense_table.get_children():
            self.expense_table.delete(row)

        # Insert all expenses into the table
        for expense in self.tracker.list_expenses():
            self.expense_table.insert("", "end", values=(expense.date, expense.category, f"${expense.amount:.2f}", expense.description))

if __name__ == '__main__':
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()
