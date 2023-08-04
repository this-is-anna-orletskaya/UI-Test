import mysql.connector
from mysql.connector import Error


class DbClient:
    
    @classmethod
    def execute_query(cls, query):
        connection = mysql.connector.connect(host="localhost", user="root", password="mypw00VA")
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed succesfully")
        except Error as e:
            print(f"The error occured: '{e}'")
        connection.close()
    
    @classmethod
    def execute_read_query(cls, query):
        connection = mysql.connector.connect(host="localhost", user="root", password="mypw00VA")
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]
        except Error as e:
            print(f"The error occured: '{e}'")
        connection.close()




    
    

