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
        print(f"Date: {transaction[0]} | "
              f"Type: {transaction[1]} | "
              f"Category: {transaction[2]} | "
              f"Amount: ₹{transaction[3]} | "
              f"Description: {transaction[4]}")

def search_transaction():
    transactions = read_transaction()
    if not transactions:
        print("\nNo transaction found\n")
        return
    keyword = input("Enter category or description to search:").strip().lower()
    found = False
    
    print("Matching transaction:\n")
    
    for transaction in transactions:
        category = transaction[2].lower()
        description = transaction[4].lower()

        if keyword in category or keyword in description:
            print(f"Date: {transaction[0]} | "
                  f"Type: {transaction[1]} | "
                  f"Category: {transaction[2]} | "
                  f"Amount: ₹{transaction[3]} | "
                  f"Description: {transaction[4]}")
            found = True

    if not found:
        print("No matching transaction found.")
