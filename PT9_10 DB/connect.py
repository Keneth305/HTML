import sqlite3 as sql # import the sqlite3 module and assign it with sql as an alias

# To use the module, start by creating a database Connection object(variable):
dbCon = sql.connect("/Users/Kenzo/Desktop/Just IT Course /HTML/PT9_10 DB/C19.db") # create and or/use db if exists

# create a cursor object to connect to the database to execute sql statemnt/queries 
dbCursor = dbCon.cursor() 