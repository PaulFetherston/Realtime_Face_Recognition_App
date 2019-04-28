import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')

    print("Retrieve data:")

    # sql_insert_query = """SELECT * FROM %s""" % (table)
    sql_insert_query = """SELECT * FROM sdptest"""

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to mysql database... MySQL Server version on ", db_Info)

        cursor = connection.cursor()
        cursor.execute(sql_insert_query)
        records = cursor.fetchall()

        print("Total number of rows = ", cursor.rowcount)
        # print("Each row's values")

        for row in records:
            print("Id = ", row[0])
            print("Name = ", row[1])

        cursor.close()


except Error as e:
    connection.rollback()  # rollback if any exceptions
    print("Error while connecting to MYSQL ", e)

finally:
    # Closing connection to db
    if (connection.is_connected()):
        connection.close()
        print("MySQL is closed")
