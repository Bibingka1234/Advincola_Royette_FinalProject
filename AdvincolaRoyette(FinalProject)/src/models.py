"""
models.py

Contains class models used in the application.
"""

from datetime import datetime


class Task:
    """
    Represents a student task.
    """

    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_complete(self):
        """
        Marks task as completed.
        """
        self.completed = True

    def to_dict(self):
        """
        Converts task object to dictionary.
        """
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }


class Expense:
    """
    Represents an expense record.
    """

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """
        Converts expense object to dictionary.
        """
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }