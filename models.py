from sqlalchemy import Column, Integer, String, Date, Numeric, Float
from sqlalchemy import MetaData, Table
from sqlalchemy.types import SMALLINT, TEXT, DECIMAL
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB

metadata = MetaData()

Payment = Table("payments", metadata, 
Column("customerNumber", Integer, primary_key=True, nullable=False),
Column("checkNumber", Integer, primary_key=True, nullable=False),
Column("paymentDate",Date, nullable=False),
Column("amount",Numeric, nullable=False)
)

Product = Table("products", metadata,
 Column("productCode", String(15), primary_key=True, nullable=False),
 Column("productName", String(70), nullable=False),
 Column("productLine", String(50), nullable=False),
 Column("productScale", String(10), nullable=False),
 Column("productVendor", String(50), nullable=False),
 Column("productDescription", TEXT, nullable=False),
 Column("quantityInStock", SMALLINT, nullable=False),
 Column("buyPrice", DECIMAL(precision=10), nullable=False),
 Column("MSRP", DECIMAL(precision=10), nullable=False)
)

ProductLine = Table("productlines", metadata,
Column("productLine", String(50), primary_key=True, nullable=False),
Column("textDescription", String(4000), nullable=True),
Column("htmlDescription", MEDIUMTEXT, nullable=True),
Column("image", MEDIUMBLOB, nullable=True)
)

Order = Table("orders", metadata,
Column("orderNumber", Integer, primary_key=True, nullable=False),
Column("orderDate", Date, nullable=False),
Column("requiredDate", Date, nullable=False),
Column("shippedDate", Date, nullable=True),
Column("status", String(15), nullable=False))

Customer = Table('customers', metadata,
        Column('customerNumber', Integer, primary_key=True),
        Column('customerName', String(50)),
        Column('contactLastName', String(50)),
        Column('contactFirstName', String(50)),
        Column('phone', String(50)),
        Column('addressLine1', String(50)),
        Column('addressLine2', String(50), nullable=True),
        Column('city', String(50)),
        Column('state', String(50), nullable=True),
        Column('postalCode', String(15), nullable=True),
        Column('country', String(50)),
        Column('salesRepEmployeeNumber', Integer, nullable=True),
        Column('creditLimit', Float(10, 2), nullable=True))

Employee = Table('employees', metadata,
        Column('employeeNumber', Integer, primary_key=True),
        Column('lastName', String(50)),
        Column('firstName', String(50)),
        Column('extension', String(10)),
        Column('email', String(100)),
        Column('officeCode', String(10)),
        Column('reportsTo', Integer, nullable=True),
        Column('jobTitle', String(50)))

Office = Table('offices', metadata,
        Column('officeCode', String(50), primary_key=True),
        Column('city', String(50)),
        Column('phone', String(50)),
        Column('addressLine1', String(50)),
        Column('addressLine2', String(50), nullable=True),
        Column('state', String(50), nullable=True),
        Column('country', String(50)),
        Column('postalCode', String(15)),
        Column('territory', String(10)))

OrderDetail = Table('orderdetails', metadata,
        Column('orderNumber', Integer, primary_key=True),
        Column('productCode', String(15), primary_key=True),
        Column('quantityOrdered', Integer),
        Column('priceEach', Float(10, 2)),
        Column('orderLineNumber', SMALLINT))


