# Jose Zamorano CYBR 410 9/19/22
# Module 6.3
from pymongo import MongoClient

    
def insert_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 

    #Creating the entrys for the collection.
    naruto = {"first_name": "Naruto", "student_id": 1010}

    #These lines insert the entries and aid with the final display of the id.
    naruto_student_id = studentCollection.insert_one(naruto).inserted_id
   

    #Printing out final details
    print("-- INSERT STATEMENT --")
    print("Inserted student record into the students collection with document_id " + str(naruto_student_id))
    




def find_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    #This will query one user. (Jacob)
    singleQuery = studentCollection.find_one({},{"_id": 0, "first_name": "Naruto", "student_id": "1010"})
    print("- - DISPLAY STUDENT TEST DOC --")
    print(singleQuery)

    
    
def find():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    #Part of the display that was requested for the assignment
    #Do while loop to display documents
    print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    #For loop to print individual output 
    for x in studentCollection.find({},{"_id": 0}):
        print(x)


def delete_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    search= {"first_name": "Naruto", "student_id": 1010}
    studentCollection.delete_one(search)

#Step 3 in the assignment
find()
#Step 4
insert_one()
#Step 5
find_one()
#step 6
delete_one()
#Step 7
find()
