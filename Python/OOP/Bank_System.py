import MySQLdb
from sqlalchemy import create_engine, MetaData, insert, update, Table, select
from BankTables import employees, customers, accounts, loans#, online


class MyDb:

    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://root:megha@localhost:3306/bank")
        self.metadata = MetaData()



class ValueError(Exception):
    pass

class Person:

    def __init__(self, first_name, last_name, phone_number, address, email_id):
        self.first_name  = first_name
        self.last_name  = last_name
        self.phone_number  = phone_number
        self.address = address
        self.email_id = email_id
    
    def update_personal_info(self, first_name, last_name, phone_number, address, email_id):
        """Upadate the personal info of a Person

        Args:
            first_name (str): first Name of the person
            last_name (str): last name of the person
            phone_number(str): phone number of the Person
            address(str): address of the Person
            email(str): email address of the person
        """

        self.first_name  = first_name
        self.last_name  = last_name
        self.phone_number  = phone_number
        self.address = address
        self.email_id = email_id

class Employee (Person):

    def __init__(self, employee_id, first_name, last_name, phone_number, address, email_id, salary):
        Person.__init__(self, first_name, last_name, phone_number, address, email_id)

        self.employee_id = employee_id

        if salary < 0:
            raise  ValueError("Salary cannot be -ve")
        else:
            self._salary =  salary

        stmt  = insert(employees).values(employee_id = self.employee_id, first_name = self.first_name, last_name = self.last_name,
                    phone_number = self.phone_number, address = self.address, email_id = self.email_id, salary = self._salary )

        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        self._salary = new_salary

    def raise_salary(self, salary_raise):
        """Raise the salary of an employee

        Args:
            employee_id (int): employee_id of an employee whose salary needs to be updated
            salary_raise (float): amount of the salary needs to be raised
        """

        if salary_raise < 0:
            raise  ValueError("Salary raise cannot be -ve")
        else:
            self._salary +=  salary_raise
            stmt  = update(employees)
            stmt = stmt.where(employees.columns.employee_id == self.employee_id)
            stmt = stmt.values(salary = self._salary)
            db = MyDb()
            connection = db.engine.connect()
            connection.execute(stmt)

    def update_personal_info(self, first_name, last_name, phone_number, address, email_id):
        """Upadate the personal info of an Employee

        Args:
            employee_id (int): employee id of an employee
            first_name (str): first Name of the person
            last_name (str): last name of the person
            phone_number(str): phone number of the Person
            address(str): address of the Person
            email(str): email address of the person
        """
        Person.update_personal_info(self, first_name, last_name, phone_number, address, email_id)
        stmt  = update(employees)
        stmt = stmt.where(employees.columns.employee_id == self.employee_id)
        stmt = stmt.values(first_name = self.first_name, last_name = self.last_name,
                    phone_number = self.phone_number, address = self.address, email_id = self.email_id, salary = self.salary )
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

class Customer (Person):

    def __init__(self, customer_id ,first_name, last_name, phone_number, address, email_id, yearly_income):
        
        Person.__init__(self, first_name, last_name, phone_number, address, email_id)
        if yearly_income < 0:
            raise  ValueError("Yearly Income cannot be -ve")
        else:
            self.yearly_income =  yearly_income

        self.customer_id = customer_id

        stmt  = insert(customers).values(customer_id = self.customer_id, first_name = self.first_name, last_name = self.last_name,
                    phone_number = self.phone_number, address = self.address, email_id = self.email_id, yearly_income = self.yearly_income )

        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)



    def update_yearly_income(self, customer_id, new_yearly_income):
        """Upadate the yearly income of a customer

        Args:
            customer_id (int): customer_id of an employee whose salary needs to be updated
            salary_raise (float): amount of the salary needs to be raised
        """
        if new_yearly_income < 0:
            raise  ValueError("new_yearly_income cannot be -ve")
        else:
            self.yearly_income =  new_yearly_income

        stmt  = update(customers)
        stmt = stmt.where(customers.columns.customer_id == self.customer_id)
        stmt = stmt.values(yearly_income = self.new_yearly_income)
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)


    def update_personal_info(self, first_name, last_name, phone_number, address, email_id, new_yearly_income):
        """Upadate the personal info of a Customer

        Args:
            customer_id (int): customer_id of a customer
            first_name (str): first Name of the customer
            last_name (str): last name of the customer
            phone_number(str): phone number of the customer
            address(str): address of the customer
            email(str): email address of the customer
        """
        Person.update_personal_info(self, first_name, last_name, phone_number, address, email_id)
        stmt  = update(customers)
        stmt = stmt.where(customers.columns.customer_id == self.customer_id)
        stmt = stmt.values(first_name = self.first_name, last_name = self.last_name,
                    phone_number = self.phone_number, address = self.address, email_id = self.email_id, yearly_income = new_yearly_income)
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

class Account():

    def __init__(self, account_id, customer_id ,balance=0):
        self.account_id = account_id
        self.customer_id = customer_id
        if balance < 0:
            raise  ValueError("balance cannot be -ve")
        else:
            self.balance = balance



    def withdraw(self ,amount):
        """withraw amount from the account

        Args:
            amount (float): amount to be withdrawn
        """
        if self.balance - amount < 0:
            raise  ValueError("balance cannot be -ve")
        else:
            self.balance -= amount

        stmt  = update(accounts)
        stmt = stmt.where(accounts.columns.account_id == self.account_id)
        stmt = stmt.values(balance = self.balance)
        
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

    def deposit(self,amount):
        """deposit amount in the account

        Args:
            amount (float): amount to be deposited
        """
        if amount < 0:
            raise  ValueError("amount cannot be -ve")
        else:
            self.balance += amount
        
        stmt  = update(accounts)
        stmt = stmt.where(accounts.columns.account_id == self.account_id)
        stmt = stmt.values(balance = self.balance)
        
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

class CheckingAccount(Account):

    def __init__(self, account_id, customer_id ,balance=0, limit=0):
        Account.__init__(self, account_id, customer_id ,balance)
        if limit < 0:
            raise  ValueError("limit cannot be -ve")
        else:
            self.limit = limit
        
        stmt  = insert(accounts).values(account_id = self.account_id, customer_id = self.customer_id ,balance = self.balance, limit = self.limit, account_type = 'Checking')

        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

    def withdraw(self,amount):
        """withraw amount from the account

        Args:
            amount (float): amount to be withdrawn
        """
        if (self.balance-amount) < self.limit:
            raise  ValueError("balance cannot be less than limit")
        else:
            self.balance -= amount

        stmt  = update(accounts)
        stmt = stmt.where(accounts.columns.account_id == self.account_id)
        stmt = stmt.values(balance = self.balance)
        
        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)


class SavingAccount(Account):

    def __init__(self, account_id, customer_id, balance=0, interest_rate=0):
        Account.__init__(self, account_id, customer_id, balance)
        if interest_rate < 0:
            raise  ValueError("interest rate cannot be -ve")
        else:
            self.interest_rate = interest_rate
        
        stmt  = insert(accounts).values(account_id = self.account_id, customer_id = self.customer_id ,balance = self.balance, interest_rate = self.interest_rate, account_type = 'Saving')

        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)

    def compute_interest(self, n_periods=1):
        """compute interst rate

        Args:
            n_periods (int) = number of periods of Saving account

        return
            total interest
        """
        return(self.balance*(1+self.interest_rate)**n_periods-1)


class Loan():

    def __init__(self, loan_id ,account_id ,loan_amount, interest_rate=0, loan_period = 1):
        self.loan_amount = loan_amount
        self.loan_period = loan_period
        self.account_id = account_id
        self.loan_id = loan_id

        if interest_rate < 0:
            raise  ValueError("interest_rate cannot be -ve")
        else:
            self.interest_rate = interest_rate

        stmt  = insert(loans).values(account_id = self.account_id, loan_id = self.loan_id ,amount = self.loan_amount, interest_rate = self.interest_rate, loan_period = self.loan_period)

        db = MyDb()
        connection = db.engine.connect()
        connection.execute(stmt)
        

    def compute_interest(self):
        """compute interst rate

        Args:
            n_periods (int) = number of periods of Saving account
        """
        return(self.loan_amount*(1+self.interest_rate)**self.loan_period-1)


class OnlineBanking():

    def __init__(self, account_id ,username, password):
        self.username = username
        self.password = password
        self.account_id = account_id

        

        db = MyDb()
        connection = db.engine.connect()
        online = Table('online_banking', db.metadata, autoload=True,
                 autoload_with=db.engine)
        stmt  = insert(online).values(account_id = self.account_id, username = self.username, password = self.password)
        connection.execute(stmt)

        
    def update_password(self, new_password):
        """update password of online banking

        Args:
            new_password (str) = new passowrd
        """
        """ Set new password """
        self.password = new_password

        
        db = MyDb()
        connection = db.engine.connect()
        online = Table('online_banking', db.metadata, autoload=True,
                 autoload_with=db.engine)
        stmt  = update(online)
        stmt = stmt.where(online.columns.account_id == self.account_id)
        stmt = stmt.values(password = new_password)
        connection.execute(stmt)

#Sam  = Customer(456, 'Paul', 'Las', '234-12', 'holly street' ,'paul@h.com', 1100 )
#Sam.update_personal_info('Paula', 'Las', '234-12', 'holly street' ,'paul@h.com', 1100)
#print(Sam.first_name)

#Sam.raise_salary(456, 2000)

ln  = Loan(456, 123, 1000, .02, 2)
print(ln.compute_interest())

