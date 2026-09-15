from tracker import ExpenseTracker
from utils import get_non_empty_text, get_positive_amount, get_positive_integer, get_valid_date, print_title


def show_menu():
    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense\n2. View Expenses\n3. Search by Category\n4. Total Expenses")
    print("5. Category Summary\n6. Delete Expense\n7. Save Data\n8. Exit")
    print("---------------------------------------------")


def read_expense_details():
    date = get_valid_date()
    category = get_non_empty_text("Category: ", "Category")
    amount = get_positive_amount()
    description = get_non_empty_text("Description: ", "Description")
    return date, category, amount, description

def run_application():
    tracker = ExpenseTracker()
    while True:
        try:
            show_menu()
            choice = get_positive_integer("Choose an option: ", "Menu choice")
            if choice == 1:
                expense = tracker.add_expense(*read_expense_details())
                print(f"Expense added successfully with ID {expense.expense_id}.")
            elif choice == 2:
                print_title("ALL EXPENSES")
                tracker.view_expenses()
            elif choice == 3:
                category = get_non_empty_text("Category to search: ", "Category")
                tracker.view_expenses(tracker.search_by_category(category))
            elif choice == 4:
                print(f"\nTotal Spending : ₹{tracker.calculate_total_expense():,.2f}")
            elif choice == 5:
                print_title("CATEGORY SUMMARY")
                summary = tracker.category_summary()
                if not summary:
                    print("No expenses found.")
                for category, amount in summary.items():
                    print(f"{category} : ₹{amount:,.2f}")
            elif choice == 6:
                expense_id = get_positive_integer("Expense ID to delete: ", "Expense ID")
                print("Expense deleted." if tracker.delete_expense(expense_id) else "Error: Expense ID not found.")
            elif choice == 7:
                tracker.save_expenses()
                print("Data saved successfully.")
            elif choice == 8:
                tracker.save_expenses()
                print("Data saved. Goodbye!")
                break
            else:
                print("Error: Please choose a valid menu option (1-8).")
        except KeyboardInterrupt:
            print("\nOperation cancelled. Your data is safe.")
        except Exception as error:
            print(f"Unexpected error handled safely: {error}")


if __name__ == "__main__":
    run_application()
