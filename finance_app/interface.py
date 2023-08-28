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

def return_table():
    return return_table_contents("portfolio", "STOCKS")
