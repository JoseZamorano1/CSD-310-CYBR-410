# Jose Zamorano CYBR 410 9/18/22
# Module 6.2
from pymongo import MongoClient



## NEW METHOD
def update_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    #Part of the display that was requested for the assignment
    studentCollection.update_one({"student_id": 1007},{"$set": {"first_name": "Zamboni"}})
    




def find_one():
    #Adding the string for the connection and using MongoClient to connect
    connection=MongoClient('mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech')
    #Connecting to the pytechDB
    pytechDB = connection["pytech"]
    #Connecting to the students collection
    studentCollection = pytechDB["students"] 
    #This will query one user. (Jacob)
    singleQuery = studentCollection.find_one({},{"_id": 0, "student_id": 1007, "first_name": "Zamboni"})
    print("- - DISPLAY STUDENT DOCUMENT FROM find_one() QUERY --")
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

#Step 4 in the assignment
find()
# Step 5 in the assignment
update_one() 
#Step 6 in the assignment
find_one()