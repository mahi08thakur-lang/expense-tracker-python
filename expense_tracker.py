
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date.strip():
        date = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            return

    category = input("Enter category (Food, Travel, Shopping, etc.): ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    print("\n--- ALL EXPENSES ---")
    for row in rows[1:]:
        print(
            f"Date: {row[0]} | Category: {row[1]} | "
            f"Description: {row[2]} | Amount: ₹{float(row[3]):.2f}"
        )

def show_total():
    total = 0.0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}")

def category_summary():
    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] = totals.get(category, 0) + amount

    print("\n--- EXPENSES BY CATEGORY ---")
    if not totals:
        print("No expenses recorded yet.")
        return

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")

def main():
    initialize_file()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()