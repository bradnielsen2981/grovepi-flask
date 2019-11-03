#----------------------------------------------------------------------------
# This code library contains all sqlite code functionality including helper functions
# Created by Brad Nielsen 2019
#----------------------------------------------------------------------------
import sqlite3, datetime

DATABASE = "test.sqlite"

# Returns a handle to the Database
def opendatabase():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row #configures database queries to return a list of dictionaries (each row/record) [{"field1":value1,"field2":value2...},{etc},{} ]
    return db

# Created a helper function so to save time and also log results
# Write your Select Query, and pass in a Tuple (a,b,c etc) representing any parameters
def ViewQueryHelper(query, params=None):
    db = opendatabase()
    cursor = db.cursor()
    result = None
    try:
        result = cursor.execute(query, params)
        result = results.fetchall()  #returns a list of dictionaries
    except (sqlite3.OperationalError, sqlite3.Warning, sqlite3.Error) as e: 
        app.logger.error("Database error: %s" % e)
        app.logger.error(query)
    db.close()
    return result #should be a list of dictionaries on success, else equals None

# Created a helper function so to save time and also log results
# Write your DELETE, INSERT, UPDATE Query, and pass in a Tuple(a,b,c etc ) representing any parameters
def ModifyQueryHelper(query, params=None):
    db = opendatabase()
    cursor = db.cursor()
    result = None
    try:
        result = cursor.execute(query, params)
    except (sqlite3.OperationalError, sqlite3.Warning, sqlite3.Error) as e: 
        app.logger.error("Database error: %s" % e)
        app.logger.error(query)
    db.commit()
    db.close()
    return result #Should be a true or false depending on success??

# NOW CREATE YOUR OWN DATABASE FUNCTIONS
# -----------------------------------------------------------------------

# Updates the users lastaccess in database
def update_access(userid):
    fmt = "%d/%m/%Y %H:%M:%S"
    datenow = datetime.now().strftime(fmt)
    ModifyQueryHelper("UPDATE users SET lastaccess = ?, active = 1 where userid = ?",(datenow, userid))
    return

# Get a list of active users from database using lastaccess field
def get_active_users():
    fmt = "%d/%m/%Y %H:%M:%S"
    users = ViewQueryHelper("SELECT username, lastaccess from users")
    activeusers = [] #blank list
    for user in users:
        td = datetime.now() - datetime.strptime(user['lastaccess'],fmt)
        if td.seconds < 120:
            activeusers.append(user['name']) #makes a list of names
    db.close()
    return activeusers #list of users