
# Paul Fetherston
#
# Student No: 2898842


import mysql.connector
from mysql.connector import Error


def db_retrieve():
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
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


def db_insert(fname, sname, dob, dept, access):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    new_user_id = 0
    try:
        print("Insert database:")

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
                new_user_id = row[0]

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
            return new_user_id


def db_search(fname, sname):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
    try:
        print("Search database:")

        sql_search_query = """SELECT id, fname, sname, dob, dept, access FROM sdptest WHERE fname="%s" AND sname="%s";
                            """ % (fname, sname)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_info)

            cursor = connection.cursor()
            cursor.execute(sql_search_query)
            records = cursor.fetchall()

            print("Total number of rows ************ = ", cursor.rowcount)
            for row in records:
                print("Id =========== ", row[0])
                print("name =========== ", row[1])
                print("last =========== ", row[2])
                print("dob =========== ", row[3])
                print("dept =========== ", row[4])
                print("Access =========== ", row[5])

            print("Searched Records")

            cursor.close()

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")
            return records


def db_id_search(user_id):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
    try:
        print("Search database:")

        sql_search_query = """SELECT id, fname, sname, dept FROM sdptest WHERE id="%i";
                            """ % user_id

        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute(sql_search_query)
            records = cursor.fetchall()

            print("Searched user id Records")

            cursor.close()

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")
            return records


def db_update(usr_id, fname, sname, dob, dept, access):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Update database:")

        sql_update_query = """UPDATE sdptest SET fname="%s", sname="%s", dob="%s", dept="%s", access="%i" 
                            WHERE id="%i";""" % (fname, sname, dob, dept, access, usr_id)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_info)

            cursor = connection.cursor()
            cursor.execute(sql_update_query)
            connection.commit()

            print("Record Updated into table")

            cursor.close()

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")


def db_user_delete(usr_id):
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Delete User database:")

        sql_delete_query = """DELETE FROM sdptest WHERE id="%i";""" % usr_id

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to mysql database... MySQL Server version on ", db_info)

            cursor = connection.cursor()
            cursor.execute(sql_delete_query)
            connection.commit()

            print("Record deleted from table")

            cursor.close()

    except Error as e:
        connection.rollback()  # rollback if any exceptions
        print("Error while connecting to MYSQL ", e)

    finally:
        # Closing connection to db
        if connection.is_connected():
            connection.close()
            print("MySQL is closed")

