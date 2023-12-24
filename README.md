## Expense Tracker

This Python script provides a simple expense-tracking system with the following features:

- Create and initialize expenses with unique IDs, titles, amounts, and timestamps.
- Update the title and/or amount of an expense.
- Retrieve expenses by ID or title.
- Add and remove expenses from the database.

## Setup Instructions
- Install Python
- Install Git
- Clone the GitHub repository:

```
git clone https://github.com/Ritnoel/AltSchool_Exam_Project.git
```
- Navigate into the AltSchool_Exam_Project directory

```
cd AltSchool_Exam_Project
```
- Run the python file

## Usage

1. Initialize expenses using the `Expense` class.

```
expense_1 = Expense(title = 'Groceries', amount = 2000)
expense_2 = Expense(title = 'Transportation', amount = 5000.50)
expense_3 = Expense(title = 'Vegetables', amount = 7000.50)
```

2. Use the `update` method to modify the title and/or amount of an expense.

```
expense_1.update(title='Groceries', amount= 3000)
```

3. Manage expenses with the `ExpenseDatabase` class by adding, removing, or retrieving expenses.

```
expense_db.add_expense(expense_1)
expense_db.add_expense(expense_2)
expense_db.expenses
```
