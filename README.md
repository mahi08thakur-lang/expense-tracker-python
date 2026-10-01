# 💰 Expense Tracker Using Python and CSV

## Project Overview

Expense Tracker is a simple, beginner-friendly Python application that helps users record and manage their daily expenses. It uses a CSV file to store expense records permanently.

## Features

* Add a new expense with date, category, description, and amount.
* View all recorded expenses.
* Calculate total expenses.
* Display category-wise expense summaries.
* Automatically save expense records in a CSV file.
* Validate dates and expense amounts.

## Technologies Used

* **Language:** Python
* **Data Storage:** CSV (Comma-Separated Values)
* **Modules:** `csv`, `os`, `datetime`

## Project Structure

```text
ExpenseTracker/
├── expense_tracker.py
├── expenses.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

* Python 3.8 or later
* No external libraries required.

## How to Run

1. Download or clone this repository.

2. Open the project folder in VS Code.

3. Open the terminal.

4. Run the command:

   `python expense_tracker.py`

5. Select an option from the menu.

6. Enter expense details when prompted.

## CSV Data Format

Expense records are stored in `expenses.csv` with the following columns:

| Date       | Category | Description | Amount |
| ---------- | -------- | ----------- | ------ |
| 2026-10-01 | Food     | Lunch       | 120.00 |
| 2026-10-01 | Travel   | Bus fare    | 40.00  |

*The examples above are illustrative.*

## Learning Outcomes

* File handling in Python
* Reading and writing CSV files
* Functions and loops
* Exception handling
* Basic data processing

## Author

Mahi

## License

This project is available for educational purposes.
