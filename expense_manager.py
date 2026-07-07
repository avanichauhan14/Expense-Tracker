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
        print("-" * 40)
        print(f"Date        : {transaction[0]}")
        print(f"Type        : {transaction[1]}")
        print(f"Category    : {transaction[2]}")
        print(f"Amount      : ₹{transaction[3]}")
        print(f"Description : {transaction[4]}")
        print("-" * 40)

def search_transaction():
    transactions = read_transaction()
    if not transactions:
        print("\nNo transaction found\n")
        return
    keyword = input("Enter category or description to search:").strip().lower()
    found = False
    
    print("Matching Transactions:\n")
    
    for transaction in transactions:
        category = transaction[2].lower()
        description = transaction[4].lower()

        if keyword in category or keyword in description:
            print("-" * 40)
            print(f"Date        : {transaction[0]}")
            print(f"Type        : {transaction[1]}")
            print(f"Category    : {transaction[2]}")
            print(f"Amount      : ₹{transaction[3]}")
            print(f"Description : {transaction[4]}")
            print("-" * 40)
            found = True

    if not found:
        print("No matching transaction found.")

def delete_transaction():
    transactions = read_transaction()
    if not transactions:
        print("\nNo transaction found\n")
        return
    
    print("\n Transactions: \n")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction}")

    try:
        choice = int(input("Enter the serial no. of transaction that you want to delete: "))
        if 1<=choice<=len(transactions):
            transactions.pop(choice-1)
            overwrite_transactions(transactions)
            print("\n Transaction deleted successfully \n")
        else:
            print("\n Invalid transaction no \n")
    except ValueError:
        print("\n Please enter a valid no. \n")

def edit_transaction():
    transactions = read_transaction()
    if not transactions:
        print("\nNo transaction found\n")
        return
    
    print("\n Transactions: \n")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction}")

    try:
        choice = int(input("Enter the serial no. of transaction that you want to edit: "))
        if 1<=choice<=len(transactions):
            print("\nEnter new details:\n")
            date = input("Enter date (format: YYYY-MM-DD): ")
            type = input("Enter (Income/Expense): ")
            category = input("Enter category: ")
            amount = input("Enter amount (in rupees): ")
            description = input("Enter description: ")

            transactions[choice-1] = [date, type, category, amount, description]
            overwrite_transactions(transactions)
            print("\n Transaction updated successfully \n")
        else:
            print("\n Invalid transaction no \n")
    except ValueError:
        print("\n Please enter a valid no. \n")
