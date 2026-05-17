"""
task_manager.py

Handles task operations.
"""

from models import Task
from storage import load_data, save_data

TASK_FILE = "data/tasks.json"


class TaskManager:
    """
    Manages task records.
    """

    def __init__(self):
        self.tasks = load_data(TASK_FILE)

    def add_task(self, title, priority):
        """
        Adds a new task.
        """
        task = Task(title, priority)
        self.tasks.append(task.to_dict())
        save_data(TASK_FILE, self.tasks)

    def view_tasks(self):
        """
        Displays all tasks.
        """
        if not self.tasks:
            print("\nNo tasks found.\n")
            return

        sorted_tasks = sorted(
            self.tasks,
            key=lambda x: x["priority"]
        )

        for index, task in enumerate(sorted_tasks, start=1):
            status = "Done" if task["completed"] else "Pending"

            print(f"""
Task #{index}
Title: {task['title']}
Priority: {task['priority']}
Status: {status}
Created: {task['created_at']}
            """)

    def complete_task(self, index):
        """
        Marks task as complete.
        """
        try:
            self.tasks[index]["completed"] = True
            save_data(TASK_FILE, self.tasks)
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task number.")