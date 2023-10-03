# import the connect .py module to add data in the songs table 
from connect import *

# create function 
def read_data():

    # select all records from the songs table
    # dbCursor.execute("SELECT * FROM songs")
    # dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
    # dbCursor.execute("SELECT ARTIST, Genre FROM songs")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre =  'Rap' or Genre = 'Afrobeat'")
    # dbCursor.execute("SELECT * FROM songs ORDER BY Artist ASC")
    
    
    

    # fetch the selected record and assigned it to the allRecords variable
    allRecords = dbCursor.fetchall()

    # loop through and display all records 
    for eachRecord in allRecords: 
        # display each record 
        print(eachRecord)

if __name__ == "__main__":
    read_data()       