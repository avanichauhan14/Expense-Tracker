import csv
import os

file_name = "expenses.csv"

header = ["Date", "Type", "Category", "Amount", "Description"]

def initialise_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)

def read_transaction():
    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)
    
def add_transaction(transaction):
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(transaction)

def overwrite_transactions(transactions):
    with open(file_name, "w", newline=""):
        writer = csv.writer
        writer.writerow(header)
        writer.writerow(transactions)