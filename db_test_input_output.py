import mysql.connector
from mysql.connector import Error


def db_retrieve():
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Retrieve data:")

        sql_query = """SELECT * FROM sdptest ORDER BY Id DESC"""

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_info)

            cursor = connection.cursor()
            cursor.execute(sql_query)
            records = cursor.fetchall()

            print("Total number of rows = ", cursor.rowcount)
            cursor.close()

        print('retrieved ******************************')

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")
            return records


def db_update(fname, sname, dob, dept, access):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Update database:")

        sql_insert_query = """INSERT INTO sdptest (fname, sname, dob, dept, access) VALUES ("%s", "%s", 
                                                    "%s", "%s", "%i")""" % (fname, sname, dob, dept, access)
        sql_user_id = """SELECT * FROM sdptest ORDER BY id DESC LIMIT 1"""

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_info)

            cursor = connection.cursor()
            cursor.execute(sql_insert_query)
            connection.commit()

            cursor.execute(sql_user_id)
            records = cursor.fetchall()

            print("Total number of rows ************ = ", cursor.rowcount)
            for row in records:
                print("Id =========== ", row[0])
                id = row[0]

            print("Record inserted into table")

            cursor.close()

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")
            return id