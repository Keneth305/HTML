# import the connect .py module to add data in the songs table 
from connect import *

# create function 
def update_data():
    # use primary key to update a record 

    idField = input("Enter SongID of the record to be updated ")

    # field to be updated 
    fieldName = input("Enter Title or Artist or Genre as field name").title()

    # field value : ask for the value Title or Artist or Genre to be updated 
    fieldValue = input(f"Enter the value for the {fieldName}field ")

    fieldValue = "'"+fieldValue+"'" # add single quotes around the field value (string)

    # update record
    dbCursor.execute(F"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idField} ")

    dbCon.commit()

    print(f"Record {idField} updated in the songs table ")



if __name__ == "__main__":
    update_data()