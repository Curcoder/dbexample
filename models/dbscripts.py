import pyodbc

conn_string = 'DRIVER={SQL Server};testserver;Database=JurgenDB;Trusted_connection=yes;'
connection = pyodbc.connect(conn_string, autocommit=True)
cursor = connection.cursor()

def create_table():
    cursor.execute("""CREATE TABLE tbJurgen(
                      id INT IDENTITY(1,1) PRIMARY KEY,
                      UserName VARCHAR(250) NOT NULL,
                      Email VARCHAR(250) NOT NULL UNIQUE,
                      Passw VARCHAR(250) NOT NULL)
                  """)
    connection.commit()
    connection.close()

def insert_user(username, email, password):
    cursor.execute("""INSERT INTO tbUsers([UserName], [Email], [Passw]) 
                      VALUES (?,?,?)""", (username, email, password))
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

def update_user(email, address, username):
    cursor.execute("UPDATE tbUsers SET [Email]=?, [Passw]=? WHERE [UserName]=?", email, password, username)
    connection.commit()
    connection.close()


# insert_user("Jesco", "jesco@hotmail.com", "test1234")
# print(get_users())