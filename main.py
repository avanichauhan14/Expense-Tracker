from storage import initialise_file
from expense_manager import(add_expense, add_income, view_transactions, search_transaction, delete_transaction, edit_transaction)

initialise_file()

print("\n-----  Hey, this is your expense tracker!!!  -----")

while True:
    print("Type 1 for Expense")
    print("Type 2 for Income")
    print("Type 3 for View Transactions")
    print("Type 4 for Search Transactions")
    print("Type 5 for Delete Transactions")
    print("Type 6 for Edit Transactions")
    print("Type 7 for Exit")
    
    choice = int(input("Enter your choice: "))
    if choice==1:
        add_expense()
    elif choice==2:
        add_income()
    elif choice==3:
        view_transactions()
    elif choice==4:
        search_transaction()
    elif choice==5:
        delete_transaction()
    elif choice==6:
        edit_transaction()
    elif choice==7:
        print("Thank you for using the expense tracker.")
        break
    else:
        print("Invalid choice")