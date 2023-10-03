# import the connect .py module to add data in the songs table 
from connect import *

# create a function  
def insert_data():
    # Note: SongID is set to autoincremnt, input/data is not required

    # ask for user input
    songTitle = input("Enter song Title: ")
    songArtist = input("Enter song Artist: ")
    songGenre = input("Enter song Genre: ")

    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES (?,?,?)",(songTitle,songArtist,songGenre))
    # or
    # dbCursor.execute("INSERT INTO songs VALUES(NULL,?,?,?),",(songTitle,songArtist,songGenre))
    dbCon.commit() # permanently write the data in the songs table in the database 

    print(f"{songArtist} inserted intp the songs table")

#  if __name__ == "__main__": will prevent the functions/method from running
# automatically when the file is imported in another file
if __name__ == "__main__":
    insert_data()