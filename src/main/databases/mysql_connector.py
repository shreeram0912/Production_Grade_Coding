from loguru import logger
import mysql.connector
from src.main.encrypt_decrypt.encrypt_decrypt import decrypt

# Create connection using functional & modular programming or Oop
class MySqlConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    # Database Connection method
    def connect(self): 
        # self object created in class MySqlConnection is pass to connect method
        # MySqlConnection Object is ready, simply we can call connect method, connection will be ready
        # Here we are reassigning self.connection which is none, with mysql connection details
        try:
            self.connection = mysql.connector.connect(host = self.config['mysql_database']['host'],
                                                user = self.config['mysql_database']['user'],
                                                password = decrypt(self.config['mysql_database']['password']),
                                                database = self.config['mysql_database']['database']
                                                )
            logger.info('MySQL Connection Successful')
        except Exception as e:
            logger.info(f'Error occurred: {e}')
            raise e
    
    # Method for close the connection
    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info('MySQL Connection closed')

# CRUD operation class
class MySQLCRUDOperation:
    def __init__(self, mysql_connection):
        self.connection = mysql_connection
    
    # Read method for reading data from mysql
    def read_from_mysql(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.info(f'Error occurred during query execution {e}')
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info('Cursor closed')
        
    # Insert method with parameters
    def insert_from_mysql(self, query, parameter):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.info(f'Error occurred during query execution {e}')
            raise e
        finally:
            self.connection.commit()

# Functional Programming
# def read_from_mysql(config, query):
#     try:
#         connection = mysql.connector.connect(host = config['mysql_database']['host'],
#                                             user = config['mysql_database']['user'],
#                                             password = decrypt(config['mysql_database']['password']),
#                                             database = config['mysql_database']['database']
#                                             )
        
#         cursor = connection.cursor() # Create cursor
#         cursor.execute(query) # Execute query
#         result = cursor.fetchall()
#         return result
#     except Exception as e:
#         logger.info(f'Error occurred in database {e}')
#         raise e
#     finally:
#         connection.commit() # To commit the insert, update, delete in database, easy for rollback
#         cursor.close() # Close the cursor
#         connection.close() # Close the connection



