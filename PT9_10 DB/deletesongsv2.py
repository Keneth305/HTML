# import the connect.py module to read data from the songs table
from connect import *

# create function 
def delete_data():
        # use primary key to delete a record
        idField = input("Enter the SongID of the record to be deleted: ")

        confirmDelete = input(f"Are you sure you want to delete {idField}: Y/N ")
        if confirmDelete == "Y":
                           
            # delete from the songs where the songid is 1/2/3/4/5......
            dbCursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
            dbCon.commit()
            
            print(f"Record {idField} deleted from the songs table")
        else:
            print(f"Your record {idField} will not be deleted")
                

if __name__ == "__main__":
        
        delete_data()
