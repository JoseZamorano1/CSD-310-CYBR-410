from pymongo import MongoClient


def insert_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 

    #Creating the entrys for the collection.
    fred = {"first_name": "Fred", "student_id": 1007}
    james = {"first_name": "James", "student_id": 1008}
    jacob = {"first_name": "Jacob", "student_id": 1009}

    #These lines insert the entries and aid with the final display of the id.
    fred_student_id = studentCollection.insert_one(fred).inserted_id
    james_student_id = studentCollection.insert_one(james).inserted_id
    jacob_student_id = studentCollection.insert_one(jacob).inserted_id

    #Printing out final details
    print("Fred has been added to the students collection with document_id " + str(fred_student_id))
    print("James has been added to the students collection with document_id " + str(james_student_id))
    print("Jacob has been added to the students collection with document_id " + str(jacob_student_id))

    print("End of program, press any key to exit")


insert_one()