from storage import read_transaction

def financial_summary():
    transactions = read_transaction()

    if not transactions:
        print("\nNo transaction found.\n")
        return
    
    total_income = 0
    total_expense = 0
    
    for transaction in transactions:
        transaction_type = transaction[1]
        amount = int(transaction[3])

        if transaction_type=="Income":
            total_income=total_income+amount
        elif transaction_type=="Expense":
            total_expense=total_expense+amount
    
    balance = total_income-total_expense

    print("\n----- REPORT -----\n")
    print(f"Total Income  : ₹{total_income}")
    print(f"Total Expense : ₹{total_expense}")
    print(f"Current Balance : ₹{balance}")
    print("---------------------\n")