"""
storage.py

Handles file storage and retrieval.
"""

import json
import os


def load_data(filename):
    """
    Loads JSON data from file.
    """
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)


def save_data(filename, data):
    """
    Saves data to JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)