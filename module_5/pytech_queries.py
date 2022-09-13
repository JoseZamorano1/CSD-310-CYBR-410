# Jose Zamorano CYBR 410 9/12/22
# importing MongoClient
from pymongo import MongoClient




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
    



def find_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    #This will query one user. (Jacob)
    singleQuery = studentCollection.find_one({},{"_id": 0, "student_id": 1009, "first_name": "Jacob"})
    print("- - DISPLAY STUDENT DOCUMENT FROM find_one() QUERY --")
    print(singleQuery)

#calling find()
find()
#calling find_one()   
find_one()