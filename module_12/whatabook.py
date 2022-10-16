import mysql.connector
from mysql.connector import errorcode
import sys

### Jose Zamorano CYBR 410 | Final Project 

#If you run in to issues executing code, please restart your IDE, I had issues with cached data when getting input from user.

## Configuration code for my mysql database (whatabook).
config = {
    "user" : "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#This is the connection string, ignore for now...
'''db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))'''

# SHOWS ALL BOOKS
def show_books():
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor=db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print(" -- DISPLAYING ALL THE BOOKS -- ")
    for book in books:
        print("Book Id: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Details: {}".format(book[2]))
        print("Author: {}".format(book[3]))
        print("\n")
    
# SHOW LOCATIONS
def show_locations():
    db = mysql.connector.connect(**config)
    
    cursor=db.cursor()
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    print(" -- DISPLAYING ALL THE STORE LOCATIONS -- ")
    for store in stores:
        print("Store ID: {}".format(store[0]))
        print("Location: {}".format(store[1]))
        print("\n")


#This menu will prompt you for your account ID and send you to the account wishlist menu
def show_account_menu():
    #The input from the last function was corrupting this input. Used sys.stdin.flush() to clear the cached data.
    
    while True:
        try:
            account_num= int(input("Please enter your account ID...  "))
            sys.stdin.flush()
            break
        except:
            print("Invalid input!")

    db = mysql.connector.connect(**config)        
    cursor=db.cursor()
    #We are querying the data in the user table where the user id equals the users input. All fields will be returned with this action.

    ## CHANGE ACCOUNT NUM TO STRING
    account_num = str(account_num)
    cursor.execute("SELECT * FROM user WHERE user_id = "+account_num)
    accounts = cursor.fetchall()
    print(" -- DISPLAYING ACCOUNT INFORMATION -- ")
    for account in accounts:
        print("User ID: {}".format(account[0]))
        print("First Name: {}".format(account[1]))
        print("Last Name: {}".format(account[2]))
        print("\n")
    
    #PASSING THE INPUT FOR THE ACCOUNT ID AND CALLING THE WISHLIST MENU
    wishlist_menu(account_num)
    
    
    #Returning account num to use in other functions.
            

def wishlist_menu(account_num):
    #The input from the last function was corrupting this input. Used sys.stdin.flush() to clear the cached data.
    
    try:
        print("--- WISHLIST MENU ---\n")
        print("OPTION 1 - WISHLIST\nOPTION 2 - ADD A BOOK TO WISHLIST\nOPTION 3 - MAIN MENU\n")
        accountNumber = account_num
        #Loop to keep the user in the program if they need to search multiple Zip Codes or City Names\
        sys.stdin.flush()
        choice = int(input("\nChoose an option..."))
        sys.stdin.flush() 
        while choice != 0:
            if choice == 1:
                print("1 - Wishlist.")
                show_wishlist(accountNumber)
                
                
            elif choice == 2:
                print('2 - Add a book to your wishlist ')
                #CALL A METHOD
                add_wishlist(accountNumber)
            
            elif choice == 3:
                print('3 - Main Menu  ')
                show_menu()

            else:
                print("\nPLEASE CHOOSE ONE OF THE PROVIDED OPTIONS!")
                print("--- WISHLIST MENU ---\n")
                print("OPTION 1 - WISHLIST\nOPTION 2 - ADD A BOOK TO WISHLIST\nOPTION 3 - MAIN MENU\n")
    
    
    except Exception as e: print(e)
        

def show_wishlist(account_num):
    db = mysql.connector.connect(**config)
    
    cursor=db.cursor()
    
    #We are querying the data in the user table where the user id equals the users input. All fields will be returned with this action.
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, books.book_id, books.book_name, books.author " +
                    "from wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN books ON wishlist.book_id = books.book_id WHERE user.user_id = "+ account_num)
    columns = cursor.fetchall()
    print(" -- DISPLAYING WISHLIST FOR ACCOUNT #"+account_num+" -- ")
    for column in columns:
        print("User ID: {}".format(column[0]))
        print("First Name: {}".format(column[1]))
        print("Last Name: {}".format(column[2]))
        print("Book ID: {}".format(column[3]))
        print("Book Name: {}".format(column[4]))
        print(" Book Author: {}".format(column[5]))
        print("\n")
    
    wishlist_menu(account_num)

def add_wishlist(account_num):
    # INSERTING SMEAGOL NEW PLAYER
    db = mysql.connector.connect(**config)
    cursor=db.cursor()
    while True:
        try:
            sys.stdin.flush()
            book_id_int = int(input("\nChoose the book ID that you want to add to your wishlist..."))
            sys.stdin.flush()
            break
        except:
            print("You did not enter a integer...")

    ## CHANGE Book ID TO STRING
    book_id = str(book_id_int)
    
    print(account_num +"\n"+ book_id)
    cursor.execute('INSERT INTO wishlist(user_id, book_id) VALUES("'+account_num+'","'+book_id+'")')
    sys.stdin.flush()
    show_menu()
    

def show_menu():
    try:
        print("Hello, welcome to my final project!\n")## RENAME PLEASE
        #Calling Menu
        
        #This will be some text that will guide the user for the menu options.
        print("Please choose one of the following options...")
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("OPTION 1 - VIEW BOOKS\nOPTION 2 - VIEW STORE LOCATIONS\nOPTION 3 - VIEW MY ACCOUNT\nOPTION 4 - EXIT PROGRAM")
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #Int will be how the user decides what option they want
        sys.stdin.flush()
        choice = int(input("\nChoose an option..."))
        sys.stdin.flush()
        #Loop to keep the user in the program if they need to search multiple Zip Codes or City Names
        while choice != 0:
            
            if choice == 1:
                print("\n1 - View books\n ")
                show_books()
                
            elif choice == 2:
                print('\n2 - View Store Locations\n  ')
                #CALL A METHOD
                show_locations()
            
            elif choice == 3:
                print('\n3 - My Account\n  ')
                #CALL A METHOD
                show_account_menu()

            elif choice == 4:
                print('\n4 - Exit Program\n  ')
                SystemExit(0)
                
                
    
            print("Please choose one of the following options...")
            print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            print("OPTION 1 - VIEW BOOKS\nOPTION 2 - VIEW STORE LOCATIONS\nOPTION 3 - VIEW MY ACCOUNT\nOPTION 4 - EXIT PROGRAM")
            print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            sys.stdin.flush()
            choice = int(input("\nChoose an option...\n"))
            sys.stdin.flush()
    except:
        print("Closing program.")

show_menu()

