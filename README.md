# Expense Tracker

This is a simple command-line Expense Tracker built using Python. This application allows users to record income and expenses, manage transactions, and generate a financial summary. Data is stored in a CSV file for persistence.


# Features

- Add Expense
- Add Income
- View All Transactions
- Search Transactions
- Edit Transactions
- Delete Transactions
- Generate Financial Summary Report
- CSV-based Data Storage


# Technologies Used

- Python 
- CSV Module
- Git
- GitHub


# Project Structure

```
Expense-Tracker/
│
├── main.py               # Entry point of the application
├── expense_manager.py    # Transaction management functions
├── storage.py            # Handles reading and writing CSV files
├── reports.py            # Financial report generation
├── .gitignore            # Files ignored by Git
├── README.md             # Project documentation
```


# How to Run

1. Clone the repository

```bash
git clone <your-repository-url>
```

2. Move into the project folder
```bash
cd Expense-Tracker
```

3. Run the program

```bash
python main.py
```


# Sample Menu
----- Expense Tracker -----

1. Add Expense
2. Add Income
3. View Transactions
4. Search Transactions
5. Delete Transaction
6. Edit Transaction
7. Generate Report
8. Exit


# Sample Report

---------- REPORT ----------

Total Income   : ₹45000
Total Expense  : ₹5000
Current Balance: ₹40000

----------------------------


# What I Learned

While building this project, I learned:

- Python file handling using the `csv` module
- Modular programming with multiple Python files
- CRUD (Create, Read, Update, Delete) operations
- Writing reusable functions
- Version control using Git
- Hosting projects on GitHub


# Future Improvements

- Monthly Expense Report
- Category-wise Expense Analysis
- Export Reports
- SQLite Database Support
- Graphical User Interface (Tkinter/PyQt)
- Authentication System


# Author

Avani Chauhan

GitHub: https://github.com/avanichauhan14
