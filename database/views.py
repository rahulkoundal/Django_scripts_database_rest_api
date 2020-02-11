"""
view.py
"""
from django.http import HttpResponse
import MySQLdb
# Create your views here.


def db_connect(request):
    """
    db db_connect
    connecting to the database
    importing MYsql for connectivity
    connect() function is used to set aup a connection
    host	127.0.0.1	The host name or IP address of the MySQL server.
    database (db*)		The database name to use when connecting with the MySQL server
    port	3306	The TCP/IP port of the MySQL server. Must be an integer.
    user (username*)		The user name used to authenticate with the MySQL server.
    password (passwd*)		The password to authenticate the user with the MySQL server.

    """
    print("request", request.user)
    try:
        db_con = MySQLdb.connect(host='localhost', database='tutorial', user='root', charset='utf8', passwd='Yukisha123@')
        print("db connectivity ", db_con)
        print("db connectivity ", type(db_con))
    except Exception as error_db_Con:
        print("error_db_Con", error_db_Con)

    return HttpResponse({"ok": "ok"})


def mysql_server_connectivity():
    db_conn = MySQLdb.connect(host='localhost', user='root', password='Yukisha123@')
    print("db_conn", db_conn)
    return db_conn


def create_database(request):
    """
    this function is used for creation a database
    :return: HttpResponse "database is create" if everything works good
    """
    try:
        db_conn = mysql_server_connectivity()
        # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        cursor = db_conn.cursor()
        # creating a database called 'datacampguide'
        # 'execute()' method is used to compile a 'SQL' statement
        # below statement is used to create tha 'datacampguide' database

        cursor.execute("CREATE DATABASE datacampguide")

    except Exception as error_create_database:
        print("error_create_database", error_create_database)

    return HttpResponse({"database is create": "database is create"})


def show_all_databases(request):
    """

    :param request:
    :return: HttpResponse "database is create" if everything works good
    """
    try:
        db_conn = mysql_server_connectivity()
        # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        cursor = db_conn.cursor()

        # 'execute()' method is used to compile a 'SQL' statement
        cursor.execute("SHOW DATABASES")
        # 'fetchall()' method fetches all the rows from the last executed statement
        databases = cursor.fetchall()  # it returns a list of all databases present
        print("type os database object", type(databases))

        # printing the list of databases
        print(list(databases))

        # showing one by one database
        for database in databases:
            print(database)

    except Exception as error_show_all_databases:
        print("show_all_databases", error_show_all_databases)

    return HttpResponse({"show_all_databases": "show_all_databases"})










