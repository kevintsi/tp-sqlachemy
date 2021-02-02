from sqlalchemy import create_engine
import subprocess

config = {
    "host" : "localhost",
    "port" : 3306,
    "user" : "root",
    "password" : "root",
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
    engine.connect()
    print("---MySQL Docker Container Python connection ok---\n")
except:
    print("Something went wrong")


subprocess = subprocess.Popen("sudo docker ps", shell=True, stdout=subprocess.PIPE)

subprocess_return = subprocess.stdout.read()

print("--- docker ps info ---")
print(subprocess_return)





