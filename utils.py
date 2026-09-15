"""Input and display helper functions for the expense tracker."""

from datetime import datetime


def get_non_empty_text(prompt, field_name):
    """Return stripped text after rejecting blank input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"Error: {field_name} cannot be empty.")


def get_valid_date(prompt="Date (YYYY-MM-DD): "):
    """Read and validate an ISO-format date, returning it as text."""
    while True:
        value = input(prompt).strip()
        try:
            return datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Error: Enter a valid date in YYYY-MM-DD format.")


def get_positive_amount(prompt="Amount: ₹"):
    """Read a positive numeric amount from the user."""
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            return amount
        except ValueError as error:
            print(f"Error: {error if str(error) else 'Enter a valid amount.'}")


def get_positive_integer(prompt, field_name="value"):
    """Read a positive integer, useful for IDs and menu choices."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                raise ValueError(f"{field_name.capitalize()} must be greater than zero.")
            return value
        except ValueError as error:
            print(f"Error: {error if str(error) else 'Enter a whole number.'}")


def print_title(title):
    """Print a consistent title separator for console sections."""
    print(f"\n{'=' * 12} {title} {'=' * 12}")
