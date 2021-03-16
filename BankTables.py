import MySQLdb
from sqlalchemy import create_engine, MetaData
from sqlalchemy import (Table, Column, String, Integer, Boolean, Float)

engine = create_engine("mysql+mysqldb://root:megha@localhost:3306/bank")
metadata = MetaData()

customers = Table("customer", metadata,
            Column('customer_id', Integer()),
            Column('first_name', String(255), nullable = False),
            Column('last_name', String(255), nullable = True),
            Column('phone_number', String(255), nullable = False),
            Column('address', String(255), nullable = False),
            Column('email_id', String(255), nullable = False),
            Column('yearly_income', Float(), nullable = False),
            Column('active', Boolean(), default=True))

employees = Table("employee", metadata,
            Column('employee_id', Integer()),
            Column('first_name', String(255), nullable = False),
            Column('last_name', String(255), nullable = True),
            Column('phone_number', String(255), nullable = False),
            Column('address', String(255), nullable = False),
            Column('email_id', String(255), nullable = False),
            Column('salary', Float(), nullable = False),
            Column('active', Boolean(), default=True))

accounts =   Table("account", metadata,
            Column('account_id', Integer()),
            Column('customer_id', Integer()),
            Column('limit', Float(), nullable = True),
            Column('balance', Float(), nullable = False),
            Column('interest_rate', Float(), nullable = True),
            Column('account_type', String(255)),
            Column('period', Integer()),
            Column('active', Boolean(), default=True))

loans =      Table("loan", metadata,
            Column('loan_id', Integer()),
            Column('account_id', Integer()),
            Column('amount', Float(), nullable = True),
            Column('interest_rate', Float(), nullable = True),
            Column('loan_period', Integer()),
            Column('active', Boolean(), default=True))

online = Table("online_banking", metadata,
            Column('account_id', Integer()),
            Column('username', String(255)),
            Column('password', String(255)),
            Column('active', Boolean(), default=True))

metadata.create_all(engine)
print(engine.table_names())