from storage import (
    add_transaction,
    read_transaction,
    overwrite_transactions
)

def add_expense():
    date = input("Enter date (format: YYYY-MM-DD): ")
    category = input("Enter expense category: ")
    amount = input("Enter amount (in rupees): ")
    description = input("Enter description: ")
    transaction = [date, "Expense", category, amount, description]
    add_transaction(transaction)
    print(" \nExpense added successfully.\n")

def add_income():
    date = input("Enter date (format: YYYY-MM-DD): ")
    category = input("Enter income category: ")
    amount = input("Enter amount (in rupees): ")
    description = input("Enter description: ")
    transaction = [date, "Income", category, amount, description]
    add_transaction(transaction)
    print(" \nIncome added successfully.\n")

def view_transactions():
    transactions = read_transaction()
    if not transactions:
        print("\nNo transaction found\n")
        return
    print("\nAll transactions:\n")
    for transaction in transactions:
        print(transaction)