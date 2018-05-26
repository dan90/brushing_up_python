'''
Created on 20 maj 2018

@author: Dan
'''
import mysql.connector
from mysql.connector import errorcode

# Creates a database object ready to fetch data from a database

class database_object(object):
    


    def __init__(self, database_address,database_name,username,password):
        '''
        Constructor
        '''
        self.database_address = database_address
        self.database_name = database_name
        self.username = username
        self.password = password
        
        try:
            self.mysql_connection =  mysql.connector.connect(user=self.username, password=self.password,
                              host=self.database_address,
                              database=self.database_name)
            self.cursor = self.mysql_connection.cursor()
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)        

    
    
    def fetch_data(self,query):
        
        self.cursor.execute(query)
        
        for row in self.cursor:
            for col in row:
                print (col)
        
        
        return
        
    
    # Closes database-connection and cursor pointer
    
    def close_connection(self):
        
        self.cursor.close()
        self.mysql_connection.close()
        
        
        
    
        
        
        
        