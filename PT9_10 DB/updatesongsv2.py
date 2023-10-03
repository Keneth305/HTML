# import the connect .py module to add data in the songs table 
from connect import *

# create function 
def update_data():
    # use primary key to update a record 

    idField = input("Enter SongID of the record to be updated ")

    # field to be updated 
    titleField = input("Enter Title value: ")
    artistField = input("Enter Artist: ")
    genreField = input("Enter Genre ")

    # add single quotes around the field value (string)
    titleField = "'"+titleField+"'"
    artistField = "'"+artistField+"'"
    genreField = "'"+genreField+"'"

    
    # update record
    dbCursor.execute(F"UPDATE songs SET title = {titleField}, Artist = {artistField}, Genre = {genreField} WHERE SongID = {idField}")


    dbCon.commit()

    print(f"Record {idField} updated in the songs table ")



if __name__ == "__main__":
    update_data()