"""
main.py

Main entry point of the application.
"""

from task_manager import TaskManager
from expense_manager import ExpenseManager
from utils import validate_number


task_manager = TaskManager()
expense_manager = ExpenseManager()


def menu():
    """
    Displays the main menu.
    """

    while True:
        print("""
================================
STUDENT TASK & EXPENSE MANAGER
================================

1. Add Task
2. View Tasks
3. Complete Task
4. Add Expense
5. View Expenses
6. Highest Expense
7. Exit

================================
        """)

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task Title: ")
            priority = input("Priority (1-5): ")

            task_manager.add_task(title, priority)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_manager.view_tasks()

            try:
                task_index = int(input("Task Number: ")) - 1
                task_manager.complete_task(task_index)

            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            category = input("Expense Category: ")

            amount = validate_number(
                input("Amount: ")
            )

            if amount is None:
                print("Invalid amount.")
            else:
                expense_manager.add_expense(category, amount)

        elif choice == "5":
            expense_manager.view_expenses()

        elif choice == "6":
            expense_manager.highest_expense()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()