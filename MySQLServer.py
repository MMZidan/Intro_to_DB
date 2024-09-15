import mysql.connector
from mysql.connector import connect, Error

def create_database():
    try:
        mydb= mysql.connector.connect(host='localhost',user='oasis',passwd='secret')

        mycursor= mydb.cursor()
        mycursor.execute("create database if not exist alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print("Error:", e)
    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    create_database()