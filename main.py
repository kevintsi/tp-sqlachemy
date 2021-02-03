from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import subprocess
from models import Payments

config = {
    "host" : "localhost",
    "port" : 3306,
    "user" : "kevin",
    "password" : "motdepasse",
    "database" : "classicmodels"
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = "mysql+pymysql://{}:{}@{}:{}/{}".format(db_user,db_pwd,db_host,db_port,db_name)
print(connection_str)
try:
    engine = create_engine(connection_str)
    conn = engine.connect()
    print("---MySQL Docker Container Python connection ok---\n")
except:
    print("Something went wrong\n")


subprocess = subprocess.Popen("sudo docker ps", shell=True, stdout=subprocess.PIPE)

subprocess_return = subprocess.stdout.read()

print("--- docker ps info ---\n")
print(subprocess_return,"\n")

print("--- Data Mapping OK ---\n")
for name in engine.table_names():
    print("- {}\n".format(name))

print("---  Selection of PAYMENTS table ---\n")
print("Type : {} \n".format(type(Payments.columns.customerNumber)))

print("Columns : {}\n\n".format(engine.table_names()))

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

print("### All payments with > 01 June 2005 : \n")
result = session.query(Payments).filter(Payments.c.paymentDate > "2005-06-01").all()

for row in result:
    print("CustomerID : {} , CheckNumber : {}, PaymentDate : {}, Amount : {}".format(row.customerNumber, row.checkNumber, row.paymentDate, row.amount))




