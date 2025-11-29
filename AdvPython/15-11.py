import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sankojuuma@25",
    database = "56r",
    port = "3306",
    autocommit = False
) 

print(conn.is_connected())

cur = conn.cursor()

cur.execute("SHOW TABLES") 
# // cur.execute(''' (for multiple lines code purpose => 3 single quotes)  ''')

# print(cur.fetchall())

# print(cur.fetchone())


# conn.close()

