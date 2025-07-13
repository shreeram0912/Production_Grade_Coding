from src.main.main import *

# Used for dry run or test any code or function
class MySqlConnection: # Reserved keyword class & MySqlConnection is class_name
    def __init__(self, config): # self means class is passing to self & config which is one argument
        self.config = config # self.config is variable which is created to assign config or argument
# which ever object is created comes in self that self need to assigned in self.config = config
my_sql_connector_object = MySqlConnection(config) # These config will come from main.py were config is created.