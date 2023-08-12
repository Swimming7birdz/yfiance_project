from database import *
from finance import *

def add_stock(stock_name, amount):
    insert_table("portfolio", "STOCKS", stock_name, amount)


def remove_stock(stock_name):
    remove_from_table("portfolio", "STOCKS", stock_name)

def view_db_tables():
    show_tables("portfolio")


def view_stocks():
    show_table_contents("portfolio", "STOCKS")

def get_stock_amount(stock_name):
    return stock_amount("portfolio", "STOCKS", stock_name)



stock_name = "VOO"
amount = 45

stock_name1 = "AAPL"
amount1 = 35

#add_stock(stock_name, amount)
#add_stock(stock_name1, amount1)
#view_stocks()


#num_shares = get_stock_amount(stock_name)
#num_shares1 = get_stock_amount(stock_name1)

print(stock_value(stock_name, amount))
print(stock_value(stock_name1, amount1))

#remove_stock(stock_name)
#remove_stock(stock_name1)






'''

print("Enter a stock:")
stock_name = input()
#stock_name = "VOO"

stock = yf.Ticker(stock_name)
check_available(stock)
    
print("Enter stock amount: ")
amount = input()
#amount = 1000

stock_value(stock, amount)
print_news_info(stock)
'''
