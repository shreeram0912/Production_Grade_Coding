# 1. Password should be in encrypted format.
# 2. Connection details should in config file in config.ini. 
# 3. Create clear function through which we can call function & return the value.
# 4. Write code in folder structure to access in another file easily.
# 5. Create main method for code & use main method to call it.
from loguru import logger
import configparser
from src.main.databases.mysql_connector import *

# Used for fetching details from config file
config = configparser.ConfigParser()
config.read(r'D:\python program\Production_coding\src\main\resources\config.ini')

def main():
    my_sql_db_connection_object = MySqlConnection(config) # Object created for class MySqlConnection
    my_sql_db_connection_object.connect()

    crud_operation_object = MySQLCRUDOperation(my_sql_db_connection_object.connection) # Object for CRUD operation
    final_result = crud_operation_object.read_from_mysql('select * from labours_table')
    logger.info(f'{final_result}')
    my_sql_db_connection_object.close_connection()

if __name__ == '__main__':
    main()

# query = "select * from labours_table"
#     final_result = my_sql_db_connection_object.read_from_mysql(config = config, query = query)
#     logger.info(f'{final_result}')


# If error = ModuleNotFoundError: No module named 'src' then {set PYTHONPATH=D:\python program\Production_coding}