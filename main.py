from sqlalchemy import create_engine
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import sessionmaker
import subprocess
from models import *

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

    subprocess = subprocess.Popen("sudo docker ps", shell=True, stdout=subprocess.PIPE)

    subprocess_return = subprocess.stdout.read()

    print("--- docker ps info ---\n")
    print(subprocess_return,"\n")

    print("--- Data Mapping OK ---\n")
    for name in engine.table_names():
        print("- {}\n".format(name))

    print("---  Selection of PAYMENTS table ---\n")
    print("Type : {} \n".format(type(Payment.columns.customerNumber)))

    print("Columns : {}\n\n".format(engine.table_names()))

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    print("### All payments with > 01 June 2005 : \n")
    result = session.query(Payment).filter(Payment.c.paymentDate > "2005-06-01").all()

    for row in result:
        print("CustomerID : {} , CheckNumber : {}, PaymentDate : {}, Amount : {}".format(row.customerNumber, row.checkNumber, row.paymentDate, row.amount))

    print("### All products: \n")

    result = session.query(Product).all()

    for row in result:
        print("{}\n".format(row))
    
    print("### 1. Préparez une liste de bureaux triés par pays, état, ville \n")

    result = session.query(Office).order_by(Office.c.country, Office.c.state, Office.c.city)


    for row in result:
        print("{}\n".format(row))

    print("### 2. Combien d'employés y-a-t-il dans l'entreprise ?\n")

    result = session.query(Employee).count()

    print("Il y a {} employés dans l'entreprise\n".format(result))

    print("### 3. Quel est le total des paiements reçus ?\n")

    result = session.query(func.sum(Payment.c.amount)).first()[0]

    print("L'entreprise a reçue un total de {} de paiements\n".format(result))

    print("### 4. Dressez la liste des lignes de produits contenant des 'Voitures'\n")

    result = session.query(ProductLine).filter(ProductLine.c.productLine.like("%Cars%"))

    for row in result:
        print("{}\n".format(row))
    
    print("### 5. Déclarez le total")
except Exception as e:
    print("Something went wrong : {}\n".format(e))
finally:
    session.close()



