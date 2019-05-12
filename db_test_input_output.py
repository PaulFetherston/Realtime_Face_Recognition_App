import mysql.connector
from mysql.connector import Error


def db_retrieve():
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
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
                print("F_Name = ", row[1])
                print("L_Name = ", row[2])
                print("DOB = ", row[3])
                print("department = ", row[4])
                print("Access Lvl = ", row[5])
                print("--------------------------------------- ")

            cursor.close()

        print('retreive ******************************')

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")


def db_update(fname, sname, dob, dept, access):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Update data:")
        name = "Bob"
        sql_insert_query = """INSERT INTO sdptest (fname, sname, dob, dept, access) VALUES ("%s", "%s", 
                                                    "%s", "%s", "%i")""" % (fname, sname, dob, dept, access)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_Info)

            cursor = connection.cursor()
            cursor.execute(sql_insert_query)
            connection.commit()

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