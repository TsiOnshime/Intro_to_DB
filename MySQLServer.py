import mysql.connector;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXIST alx_book_store")
    print("Database 'alx_book_store' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")