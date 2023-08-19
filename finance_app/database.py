import mysql.connector

'''
# To connect MySQL database
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password = "Port404",
        )

    print(mydb)
    mycursor = mydb.cursor()

    mycursor.execute("DROP database IF EXISTS portfolio")
    #dropping portfolio database if it already exists

    mycursor.execute("CREATE DATABASE portfolio")
    print(mycursor.execute("SHOW DATABASES"))
    print(mycursor.fetchall())

    mydb.close()

#To connect ot MySQL database
def create_table(db_name, table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password = "Port404",
        database = db_name
        )

    mycursor = mydb.cursor()

    sql_statement = "DROP TABLE IF EXISTS " + table_name
    mycursor.execute(sql_statement)
    #dropping STOCKS table if it already exists

    sql_statement = "CREATE TABLE STOCKS (NAME CHAR(20) NOT NULL, AMOUNT INT)"
    mycursor.execute(sql_statement)

    mydb.close()
'''

def show_tables(db_name):
    mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for table_name in mycursor:
        print(table_name)

    mycursor.close() 
    mydb.close()


def show_table_contents(db_name, table_name):
    myresult = return_table_contents(db_name, table_name)

    if len(myresult) == 0:
        print("The Database is empty!")

    else:
        for row in myresult:
            print(row)

    
def return_table_contents(db_name, table_name):
    mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    slq_show_all = "SELECT * FROM " + table_name
    mycursor.execute(slq_show_all) 
    myresult = mycursor.fetchall()

    mycursor.close() 
    mydb.close()

    return myresult


def insert_table(db_name, table_name, stock_name, num_shares):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    sql_insert = ("INSERT INTO " + table_name + 
    "(name, amount)"
    "VALUES(%s, %s)")

    stock_summary = (stock_name, num_shares)
    
    try:
        mycursor.execute(sql_insert, stock_summary)
        mydb.commit()
        print("Record inserted " + stock_name + " with " + str(num_shares) + " number of shares")
    
    except:
        mydb.rollback()
        print("Insertion Failed")

    mycursor.close() 
    mydb.close()   
    
    
def stock_amount(db_name, table_name, stock_name):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    if db_contains(db_name, table_name, stock_name) == True:
        VALUE = "AMOUNT"
        KEY = "NAME"
        sql_show_stock = "SELECT " + VALUE + " FROM " + table_name + " WHERE " + KEY + " = '" + stock_name + "'"

        try:
            mycursor.execute(sql_show_stock)
            num_shares = mycursor.fetchone()
            return num_shares[0]
        
        except:
            mydb.rollback()
            print("Can't retrieve" + stock_name + "amount")

    mycursor.close() 
    mydb.close()   


def remove_from_table(db_name, table_name, stock_name):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    if db_contains(db_name, table_name, stock_name) == True:
        KEY = "NAME"
        sql_remove = "DELETE FROM " + table_name + " WHERE " + KEY + " = %s"
        name = (stock_name, )

        try:
            mycursor.execute(sql_remove, name)
            mydb.commit()
            print("Deleted " + stock_name + " from database")

        except:
            mydb.rollback()
            print("Deletion Failed")

    mycursor.close() 
    mydb.close()    


def update_table(db_name, table_name, stock_name, num_shares):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    if db_contains(db_name, table_name, stock_name) == True:
        VALUE = "AMOUNT"
        KEY = "NAME"

        sql_update = "UPDATE " + table_name + " SET " + VALUE + " = %s WHERE " + KEY + " = %s"
        stock_update = (num_shares, stock_name)

        try:
            mycursor.execute(sql_update, stock_update)
            mydb.commit()
            print("Updated " + stock_name + " number of shares to " + str(num_shares))
        
        except:
            mydb.rollback()
            print("Update Failed")

    mycursor.close()
    mydb.close()


def db_contains(db_name, table_name, stock_name) -> bool:
    mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    KEY = "NAME"

    slq_check = "SELECT * FROM " + table_name + " WHERE " + KEY + " = %s"
    name = (stock_name, )

    try:
        mycursor.execute(slq_check, name) 
        result = mycursor.fetchall()
        
        if len(result) == 1:
            return True

        elif len(result) > 1:
            print(stock_name + " appears multiple times in Database")
            return True

        else:
            print(stock_name + " not in Database")
            return False

    except:
        print("Check Failed")

    mycursor.close()
    mydb.close()
        