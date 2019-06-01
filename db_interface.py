
# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

import mysql.connector
from mysql.connector import Error


def db_retrieve():
    """Method to return all records from the database"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
    try:
        print("Retrieve data:")

        sql_query = """SELECT * FROM sdptest ORDER BY Id DESC"""

        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute(sql_query)
            records = cursor.fetchall()
            cursor.close()

        print('All data retrieved')

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
    """Method to to insert new user to the db and return the new users unique id"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    new_user_id = 0
    try:
        print("Insert database:")

        sql_insert_query = """INSERT INTO sdptest (fname, sname, dob, dept, access) VALUES ("%s", "%s", 
                                                    "%s", "%s", "%i")""" % (fname, sname, dob, dept, access)
        sql_user_id = """SELECT * FROM sdptest ORDER BY id DESC LIMIT 1"""

        if connection.is_connected():
            # insert new user info
            cursor = connection.cursor()
            cursor.execute(sql_insert_query)
            connection.commit()
            # Retrieve the new users ID
            cursor.execute(sql_user_id)
            records = cursor.fetchall()
            # Assign the new users id to be returned
            for row in records:
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
    """Method to search the db for an existing user
    - If found return the users information"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
    try:
        print("Search database:")

        sql_search_query = """SELECT id, fname, sname, dob, dept, access FROM sdptest WHERE fname="%s" AND sname="%s";
                            """ % (fname, sname)

        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute(sql_search_query)
            records = cursor.fetchall()

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
    """Method to search the db based on the users id"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    records = 0
    try:
        print("Search database:")

        sql_search_query = """SELECT id, fname, sname, dept, access FROM sdptest WHERE id="%i";
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
    """Method to update a pre-existing user in the db"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Update database:")

        sql_update_query = """UPDATE sdptest SET fname="%s", sname="%s", dob="%s", dept="%s", access="%i" 
                            WHERE id="%i";""" % (fname, sname, dob, dept, access, usr_id)

        if connection.is_connected():

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
    """Method to delete a user from the db"""
    connection = mysql.connector.connect(host='localhost', database='test', user='root', password='Jennifer1')
    try:
        print("Delete User database:")

        sql_delete_query = """DELETE FROM sdptest WHERE id="%i";""" % usr_id

        if connection.is_connected():

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

