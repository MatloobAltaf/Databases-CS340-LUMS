# this file creates a new database using create_db.sql

import mysql.connector as connector
import PyInquirer as pypi


mydb = connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Ptg61mysql"
)
cursor = mydb.cursor()

filename = "create-db.sql"
fd = open(filename, 'r')
sqlFile = fd.read()
fd.close()
# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')
# Execute every command from the input file
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        cursor.execute(command)
    except IOError as msg:
        print ("Command skipped: ", msg)
mydb.commit()