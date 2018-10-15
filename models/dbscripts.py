import pyodbc

conn_string = 'DRIVER={SQL Server};Server=TESTSERVER;Database=TESTDB;Trusted_connection=yes;'
connection = pyodbc.connect(conn_string, autocommit=True)
cursor = connection.cursor()

def create_table():
    cursor.execute("""CREATE TABLE tbUsers(
                      id INT IDENTITY(1,1) PRIMARY KEY,
                      Name VARCHAR(250) NOT NULL,
                      Email VARCHAR(250) NOT NULL UNIQUE,
                      Address VARCHAR(250) NOT NULL)
                  """)
    connection.commit()
    connection.close()

def insert_user(name, email, address):
    cursor.execute("""INSERT INTO tbUsers([Name], [Email], [Address]) 
                      VALUES (?,?,?)""",
                    (name, email, address))
    connection.commit()
    connection.close()

def get_users():
    cursor.execute("SELECT * FROM tbUsers")
    rows = cursor.fetchall()
    connection.close()
    return rows[0]

def delete_user(email):
    cursor.execute("DELETE FROM tbUsers WHERE [Email]=?", email)
    connection.commit()
    connection.close()

def update_user(email, address, name):
    cursor.execute("UPDATE tbUsers SET [Email]=?, [Address]=? WHERE [Name]=?", email, address, name)
    connection.commit()
    connection.close()

