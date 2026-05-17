"""
expense_manager.py

Handles expense tracking operations.
"""

from models import Expense
from storage import load_data, save_data

EXPENSE_FILE = "data/expenses.json"


class ExpenseManager:
    """
    Manages expense records.
    """

    def __init__(self):
        self.expenses = load_data(EXPENSE_FILE)

    def add_expense(self, category, amount):
        """
        Adds expense record.
        """
        expense = Expense(category, amount)
        self.expenses.append(expense.to_dict())
        save_data(EXPENSE_FILE, self.expenses)

    def view_expenses(self):
        """
        Displays all expenses.
        """
        if not self.expenses:
            print("\nNo expenses found.\n")
            return

        total = 0

        for expense in self.expenses:
            print(f"""
Category: {expense['category']}
Amount: PHP {expense['amount']}
Date: {expense['date']}
            """)
            total += expense["amount"]

        print(f"\nTotal Expenses: PHP {total}")

    def highest_expense(self):
        """
        Finds highest expense using max().
        """
        if not self.expenses:
            print("No expenses available.")
            return

        highest = max(
            self.expenses,
            key=lambda x: x["amount"]
        )

        print(f"""
Highest Expense:
Category: {highest['category']}
Amount: PHP {highest['amount']}
        """)