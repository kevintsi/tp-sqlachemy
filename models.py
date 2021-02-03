from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy import MetaData, Table

metadata = MetaData()

Payments = Table("payments", 
metadata, 
Column("customerNumber", Integer, primary_key=True, nullable=False),
Column("checkNumber", Integer, primary_key=True, nullable=False),
Column("paymentDate",Date, nullable=False),
Column("amount",Numeric, nullable=False)
)