from database import *
from finance import *

def add_stock(stock_name, num_shares):
    insert_table("portfolio", "STOCKS", stock_name, num_shares)

def remove_stock(stock_name):
    remove_from_table("portfolio", "STOCKS", stock_name)

def get_stock_amount(stock_name):
    return stock_amount("portfolio", "STOCKS", stock_name)

def update_stock_amount(stock_name, num_shares):
    update_table("portfolio", "STOCKS", stock_name, num_shares)

def verify_stock(stock_name):
    return db_contains("portfolio", "STOCKS", stock_name)


def view_db_tables():
    show_tables("portfolio")

def view_table():
    show_table_contents("portfolio", "STOCKS")



stock_name = "VOO"
ticker_exists(stock_name)
amount = 45


stock_name1 = "T"
ticker_exists(stock_name1)
amount1 = 35

stock_name2 = "AAPL"


stock_list = [stock_name, stock_name1, stock_name2]
compare_stocks(stock_list)

'''
add_stock(stock_name, amount)
view_table()

if verify_stock(stock_name) == True:
    update_stock_amount(stock_name, 55)
    num_shares = get_stock_amount(stock_name)
    value_share = stock_value(stock_name)
    total_value_shares = total_stock_value(value_share, amount)
    print(value_share)
    print(total_value_shares)


if verify_stock(stock_name1) == True:
    update_stock_amount(stock_name1, 100)
    num_shares1 = get_stock_amount(stock_name1)
    print(stock_value(stock_name1))

view_table()

remove_stock(stock_name)
remove_stock(stock_name1)

view_table()

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