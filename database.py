#----------------------------------------------------------------------------
# This Database object provides an interface to the database and includes logging
# I have made this an object because you could have more than one database in your system
# It's therefore easier to simply inherit the code..
# Created by Brad Nielsen 2019
#----------------------------------------------------------------------------
import sqlite3
import logging

class DatabaseHelper():

    def __init__(self, location):
        self.location = location #location of database file
        self.log = logging.getLogger('app') #pass in a function to handle errors (app.logger.error from Flask)
        return

    # Returns a handle to the Database 
    def connect(self):
        connection = sqlite3.connect(self.location)
        connection.row_factory = sqlite3.Row #configures database queries to return a list of dictionaries (each row/record) [{"field1":value1,"field2":value2...},{etc},{} ]
        return connection

    # A helper function to save time and also log sql errors
    # Write your Select Query, and pass in a Tuple (a,b,c etc) representing any parameters
    def ViewQueryHelper(self, query, params=None):
        connection = self.connect()
        result = None
        try:
            cursor = connection.execute(query, params)
            result = cursor.fetchall()  #returns a list of dictionaries
        except (sqlite3.OperationalError, sqlite3.Warning, sqlite3.Error) as e:
            self.log.error(query) 
            self.log.error("Database error: %s" % e)
        connection.close()
        return result #should be a list of dictionaries on success, else equals None

    # Created a helper function so to save time and also log results
    # Write your DELETE, INSERT, UPDATE Query, and pass in a Tuple(a,b,c etc ) representing any parameters
    def ModifyQueryHelper(self, query, params=None):
        connection = self.connect()
        result = None
        try:
            result = connection.execute(query, params)
        except (sqlite3.OperationalError, sqlite3.Warning, sqlite3.Error) as e:
            self.log.error(query) 
            self.log.error("Database error: %s" % e)
        connection.commit()
        connection.close()
        return result #Should be a true or false depending on success??

# Close Database Class --------------------------------------------
