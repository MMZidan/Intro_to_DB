import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

try:
    # Establish a connection to the MySQL database
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database=input("Enter Database name: ")
    ) as connection:
        print("Connection established:", connection)

        # Get server info
        print("Server version:", connection.get_server_info())

        # Create a cursor object
        with connection.cursor() as mycursor:
            # Execute a query
            mycursor.execute("SELECT * FROM authors WHERE first_name = %s", ('George',))
            myresult = mycursor.fetchall()

            # Print the results
            for row in myresult:
                print(row)

except Error as e:
    print("Error:", e)


mycursor.close()
mycursor.close()