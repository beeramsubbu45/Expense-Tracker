import json
from collections import defaultdict
from json import JSONDecodeError

from expense import Expense


class ExpenseTracker:
    """Manage expense objects, JSON persistence, and report calculations."""

    def __init__(self, filename="expenses.json"):
        """Initialise an empty expense list and load saved data."""
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from JSON, creating a valid empty file when needed."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict):
                expense_data = data.get("expenses", [])
            elif isinstance(data, list):  # Supports the simplest JSON format too.
                expense_data = data
            else:
                raise JSONDecodeError("Invalid JSON structure", "", 0)
            self.expenses = [Expense.from_dict(item) for item in expense_data]
            print(f"Loaded {len(self.expenses)} expense(s).")
        except FileNotFoundError:
            print("No data file found. Creating a new expenses.json file.")
            self.save_expenses()
        except JSONDecodeError:
            print("Warning: JSON data is invalid. Starting with an empty tracker.")
            self.expenses = []
            self.save_expenses()
        except (KeyError, TypeError, ValueError) as error:
            print(f"Warning: Could not read saved expenses: {error}")
            self.expenses = []

    def save_expenses(self):
        """Write the current expense list to JSON."""
        data = {"expenses": [expense.to_dict() for expense in self.expenses]}
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except OSError as error:
            print(f"Error: Could not save data: {error}")

    def generate_next_id(self):
        """Return the next unused numeric expense ID."""
        return max((expense.expense_id for expense in self.expenses), default=0) + 1

    def add_expense(self, date, category, amount, description):
        """Create, store, and automatically save a new expense."""
        expense = Expense(self.generate_next_id(), date, category, amount, description)
        self.expenses.append(expense)
        self.save_expenses()
        return expense

    def view_expenses(self, expenses=None):
        """Display all expenses, or a supplied filtered collection."""
        expenses_to_show = self.expenses if expenses is None else expenses
        if not expenses_to_show:
            print("No expenses found.")
            return
        for expense in expenses_to_show:
            expense.display()

    def search_by_category(self, category):
        """Return expenses whose category matches without case sensitivity."""
        return [item for item in self.expenses if item.category.lower() == category.lower()]

    def calculate_total_expense(self):
        """Calculate the total of every stored expense."""
        return sum(item.amount for item in self.expenses)

    def category_summary(self):
        """Return a dictionary mapping categories to their total spending."""
        summary = defaultdict(float)
        for item in self.expenses:
            summary[item.category] += item.amount
        return dict(summary)

    def get_expense_by_id(self, expense_id):
        """Find one expense by ID, returning None when it does not exist."""
        return next((item for item in self.expenses if item.expense_id == expense_id), None)

    def delete_expense(self, expense_id):
        """Remove an expense by ID and save only when it exists."""
        expense = self.get_expense_by_id(expense_id)
        if expense is None:
            return False
        self.expenses.remove(expense)
        self.save_expenses()
        return True
