import psycopg2

#Configuracao Database PostgreSQL (Alterar conforme configuracao do banco)
host='localhost'
database='teste'
user='dba'
password='mobile'

con = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = con.cursor()

def getConnection():
    return con

def getCursor():
    return cur    

def closeConnection():
    con.close()    