import mysql.connector

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


def show_tables(db_name):
    mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for table_name in mycursor:
        print(table_name)

    mycursor.close() 
    mydb.close()


def show_table_contents(db_name, table_name):
    mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    slq_show_all = "SELECT * FROM " + table_name
    mycursor.execute(slq_show_all) 
    myresult = mycursor.fetchall()

    #add function to print if table is empty

    for row in myresult:
        print(row)

    mycursor.close() 
    mydb.close()
    

def insert_table(db_name, table_name, stock_name, amount):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()

    sql_insert = ("INSERT INTO " + table_name + 
    "(name, amount)"
    "VALUES(%s, %s)")

    stock_summary = (stock_name, amount)
    
    try:
        mycursor.execute(sql_insert, stock_summary)
        mydb.commit()
        print("Record inserted " + stock_name + " with " + str(amount) + " number of shares")
    
    except:
        mydb.rollback()
        print("Insertion Failed")

    mycursor.close() 
    mydb.close()   
    
    
def stock_amount(db_name, table_name, stock_name):
    mydb = mydb = mysql.connector.connect(host="localhost", user="root",  password = "Port404", database = db_name)
    mycursor = mydb.cursor()


    Value = "AMOUNT"
    key = "NAME"
    sql_show_stock = "SELECT " + Value + " FROM " + table_name + " WHERE " + key + " = '" + stock_name + "'"

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

    sql_remove = "DELETE FROM " + table_name + " WHERE NAME = '" + stock_name + "'"
    
    
    try:
        mycursor.execute(sql_remove)
        mydb.commit()
        print("Deleted " + stock_name + " from database")
    
    except:
        mydb.rollback()
        print("Deletion Failed")

    mycursor.close() 
    mydb.close()    


'''def update_table(db_name, table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password = "Port404",
        database = db_name
        )
    mycursor = mydb.cursor()
'''