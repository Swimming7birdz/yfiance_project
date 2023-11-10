# Stock Assistant app

## **Description** 
Stock Assistance Desktop application compares stock metrics, tracks shares, and reports their value.
Uses yfinance retrieves data from Yahoo finance and pandas visualizes and analyzes information.
App utilizes mySQL database to store user info.

## **User Guide**
+ Database fields: stock ticker name and number of stocks
  - Note: database is meant to only hold once instance of each share

+ For simplicity database functions can be accessed through an interface, while finance functions can be accessed directed
+ Comparing shares by manually searching them up <br />
```
#COMPARING STOCKS EXAMPLE
stock_name = "TSLA"
ticker_exists(stock_name)

stock_name1 = "T"
ticker_exists(stock_name1)

stock_name2 = "AAPL"
ticker_exists(stock_name2)

stock_list = [stock_name, stock_name1, stock_name2]
compare_stocks(stock_list)
```
+ Comparing shares in database <br />
```
#Database contents
#('VOO', 45)
#('MMM', 30)

#COMPARING DATABASE STOCKS EXAMPLE
db_compare_stocks(table_list())
```

+ Metrics for comparing stocks:
   - opening price
   - previous closing price
   - 50 day average
   - 200 day average
   - year change in price
   - year high in price
   - year low in price

## **Limitations**
1. Stocks information is limited to what Yahoo Finance provides
2. Furthermore certain shares or share information may be unavailable
3. Stock values may not be accurate as yfinance supplies share prices only when markets are open 

## **Language Requirements**
+ Python3 <br />
+ MySQl <br />

## **Library Requirements** 
+ yfinance <br />
+ Pandas <br />
+ Numpy <br />
+ Matplotlib <br />

## **Updates**
+ 11/5: .info returns errors, temporarily replaced with .fast_info (yfinance)
  - while .fast_info provides less information, this is the only viable solution for the time

### **Important links**
+ [yfinance documentation](https://pypi.org/project/yfinance)
+ [pandas documentation(api)](https://pandas.pydata.org/docs/reference/index.html)
+ [pandas documentation(user-guide)](https://pandas.pydata.org/docs/user_guide/index.html)

## **Setting up MySQL Database**
```
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
```

