from __future__ import annotations

class Expense:
    def __init__(self, expense_id, date, category, amount, description):
        self.expense_id = int(expense_id)
        self.date = str(date)
        self.category = str(category)
        self.amount = float(amount)
        self.description = str(description)

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["expense_id"],
            data["date"],
            data["category"],
            data["amount"],
            data["description"],
        )

    def display(self):
        print("---------------------------------------")
        print(f"Expense ID : {self.expense_id}")
        print(f"Date       : {self.date}")
        print(f"Category   : {self.category}")
        print(f"Amount     : ₹{self.amount:,.2f}")
        print(f"Description: {self.description}")
        print("---------------------------------------")
