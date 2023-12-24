from uuid import uuid4
from datetime import datetime


""" This method initializes the Expense attributes """
class Expense:
    def __init__(self, title, amount):
        
        self.id = str(uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    '''This method allows updating the title and/or amount of the expense'''
    def update(self, title = None, amount = None):
        
        self.title = title
        self.amount = amount
        self.updated_at = datetime.utcnow()
        return f"title: {self.title}, amount: {self.amount} has been updated"
    
        '''This method returns a dictionary representation of the expense'''
    def to_dict(self):
        
        expense_dict = {'id': self.id, 'title': self.title, 'amount': self.amount, 'created_at': str(self.created_at), 'updated_at': str(self.updated_at)}
        return expense_dict
    
        '''This method initializes the expense list'''
class ExpenseDatabase:
    def __init__(self):
        
        self.expenses = []

        '''This method adds an expense to the database'''
    def add_expense(self, expense):
        
        self.expenses.append(expense.to_dict())
        print('expense added successfully!')
 
        '''This method removes an expense from the database'''
    def remove_expense(self, expense_id):
        
        self.expenses = [item_expense for item_expense in self.expenses if item_expense['id'] != expense_id]
        print(f"{expense_id} successfully removed!")
        
        '''This method retrieves an expense by ID'''
    def get_expense_by_id(self, expense_id):
       
        for item_expense in self.expenses:
            if item_expense['id'] == expense_id:
                return item_expense
                break
        
        '''This method retrieves an expense by title and returns a list'''
    def get_expense_by_title(self, expense_title):
        
        return [item_expense for item_expense in self.expenses if item_expense['title'] == expense_title]
        
        '''This method returns a list of dictionaries representing each expense in the database'''
    def to_dict(self): 
        
        return self.expenses

expense_1 = Expense(title = 'Out_of_pocket', amount = 2000)
expense_2 = Expense(title = 'Fuel', amount = 5000.50)
expense_db = ExpenseDatabase()

# expense_1 = Expense(title = 'Out_of_pocket', amount = 2000)
# expense_2 = Expense(title = 'Fuel', amount = 5000.50)
# expense_3 = Expense(title = 'Fuel', amount = 7000.50)
# print(expense_1.update(title='Out_of_pocket', amount= 3000))

# print(expense_1.to_dict())
# print(expense_2.to_dict())
# print(expense_3.to_dict())

# expense_db.add_expense(expense_1)
# expense_db.add_expense(expense_2)
# print(expense_db.expenses)  


