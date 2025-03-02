import mysql.connector


def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="notSecureChangeMe",
        database="customers"
    )
