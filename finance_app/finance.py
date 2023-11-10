import yfinance as yf
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_ticker(stock_name):
    return yf.Ticker(stock_name)

def print_news_info(stock_name): #returns every article (with their title and link) regarding stock_name
    stock = create_ticker(stock_name)
    news_info_list = stock.news
    for article_info_map in news_info_list:
        print("Title: " + article_info_map.get('title'))
    
        print("Link to Article: " + article_info_map.get('link'))
        print()

def ticker_exists(stock_name): #Checks if stock_name is available via the Yahoo Finance API.
    stock = create_ticker(stock_name)

    info = stock.history(period='7d', interval='1d')
    
    if len(info) <= 0:
        sys.exit("Invalid Stock Name")
    

def stock_value(stock_name): #Returns current market value of stock and the sum of n-amount of this stock
    stock = create_ticker(stock_name)

    #need to return price at closing when markets are closed

    try:
        data = stock.history(period="1d", interval="1m")
        curr_value = data["Close"].iloc[-1]
        #returns accurate price when markets are up
        #returns stock price 2-5 minutes before markets closed 
        return curr_value

        #ticker.info will return current value? consider using that instead!

    except IndexError:
        sys.exit("Error occurred, terminating stock value calculation")

    
def total_stock_value(curr_value, amount): #calculate total value of stock_name
    return float(curr_value) * float(amount)


def stock_stats(stock_name): #return a list with all the stock's metrics: 52 week high-lo-change, open, high, low, close, dividend-rate-yield-annual
    stock = create_ticker(stock_name)

    try:
         #[11/5] .info returns errors, using .fast_info 
        complete_stock_data = stock.fast_info 
    except:
        sys.exit("Data can't be retrieved at the moment")

    stock_info = {}
    metrics = ["fiftyTwoWeekLow","fiftyTwoWeekHigh","52WeekChange","previousClose","open","dayLow","dayHigh","currentPrice","dividendRate","dividendYield","trailingAnnualDividendRate","trailingAnnualDividendYield"]
    
    #[11/5] .info returns errors, using .fast_info 
    fast_metrics = ["open", "previousClose", "fiftyDayAverage", "twoHundredDayAverage", "yearChange", "yearHigh", "yearLow"]

    for metric in fast_metrics: #replacing metric
        try:
            stock_info[metric] = complete_stock_data.get(metric)
        except:
            sys.exit("Data can't be retrieved at the moment")

    return stock_info #list with 52 week high-lo-change, open, high, low, close, dividend-rate-yield-annual
    
def compare_stocks(stock_list): #prints the data metrics of stocks in stock_list and generates graph to compare their data metrics
    ''' [11/5] .info returns errors, using .fast_info 
    weekLow, weekHigh, weekChange = [], [], []
    prevClose, open, low, high, price = [], [], [], [], []
    dvRate, dvYield, annDvYield, annDvRate = [], [], [], []
    '''

    open, previousClose = [], []
    fiftyDayAverage, twoHundredDayAverage = [], []
    yearChange, yearLow, yearHigh = [], [], []

    ''' [11/5] .info returns errors, using .fast_info 
    metrics = ["fiftyTwoWeekLow","fiftyTwoWeekHigh","52WeekChange","previousClose","open","dayLow","dayHigh","currentPrice","dividendRate","dividendYield","trailingAnnualDividendRate","trailingAnnualDividendYield"]
    metric_lists = [weekLow, weekHigh, weekChange, prevClose, open, low, high, price, dvRate, dvYield, annDvRate, annDvYield]
    '''

    fast_metrics = ["open", "previousClose", "fiftyDayAverage", "twoHundredDayAverage", "yearChange", "yearHigh", "yearLow"]
    fast_metric_lists = [open, previousClose, fiftyDayAverage, twoHundredDayAverage, yearChange, yearLow, yearHigh]

    metric_data = list(zip(fast_metrics, fast_metric_lists)) #replace with fast_metrics, and fast_metric_lists

    for stock_name in stock_list:
        stock_info = stock_stats(stock_name)

        for metric, metric_list in metric_data:
            if stock_info.get(metric) == None: metric_list.append(np.nan)
            else: metric_list.append(stock_info.get(metric))            

    '''
    data = {
        "fiftyTwoWeekLow": weekLow,
        "fiftyTwoWeekHigh": weekHigh,
        "52WeekChange": weekChange,
        "previousClose": prevClose,
        "open": open,
        "low": low,
        "high": high,
        "currentPrice": price,
        "dividendRate": dvRate,
        "dividendYield": dvYield,
        "trailingAnnualDividendRate": annDvRate,
        "trailingAnnualDividendYield": annDvYield
    }
    '''

    fast_data = {
        "open": open,
        "previousClose": previousClose,
        "fiftyDayAverage": fiftyDayAverage,
        "twoHundredDayAverage": twoHundredDayAverage,
        "yearChange": yearChange,
        "yearLow": yearLow,
        "yearHigh": yearHigh
    }

    dataFrame = pd.DataFrame(fast_data, index=stock_list)

    #for each stock, call stock_stats and put returned list into conresponding pd.series (name, open, high, low, close)
    print(dataFrame)
    print()
    print(dataFrame.describe())
    #visualize_stocks(dataFrame)


def db_stock_stats(stock_name, amount):
    stock_info = {}
    curr_price = stock_value(stock_name)
    stock_info["amount"] = amount
    stock_info["sharePrice"] = curr_price
    stock_info["totalShareValue"] = total_stock_value(curr_price, amount)

    # amount of shares, share price, total_stock value
    return stock_info


def db_compare_stocks(db_list): #prints the data metrics of stocks in the database and generates graph to compare their data metrics
    #db_list is list (of tuples) which contains the stock name and share amount [must call return_table]
    share_amount, share_price, total_share_value = [], [], []
    all_stock_names = []

    for db_info in db_list:
        stock_name = db_info[0]
        all_stock_names.append(stock_name)
        amount = db_info[1]

        db_stock_info = db_stock_stats(stock_name, amount)
        share_amount.append(db_stock_info.get("amount"))
        share_price.append(db_stock_info.get("sharePrice"))
        total_share_value.append(db_stock_info.get("totalShareValue"))

    data = {
        "amount": share_amount,
        "sharePrice": share_price,
        "totalShareValue": total_share_value
    }

    
    #for each stock call db_stock_stats and put returned list into corresponding pd.series
    dataFrame = pd.DataFrame(data, index=all_stock_names)
    
    print(dataFrame)
    print()
    print(dataFrame.describe())
    analyze_stock(dataFrame)
    #visualize_stocks(dataFrame)

def analyze_stock(dataFrame):
    dataFrame['default_rank'] = dataFrame['totalShareValue'].rank(method='max')
    print(dataFrame)


def visualize_stocks(dataFrame):#generates graph of stock data metrics (name is x-axis)
    try:
        dataFrame.plot.bar(rot = 0)

        plt.xlabel('Ticker')
        plt.show()

    except:
        print("Graph failed to generate")

'''
MORE yFinance Functions:

print_news_info(stock.news)

print(stock.history(period="1mo")) #lists dates, open, high, low, close, volume, dividends, and stock splits

print(stock.history_metadata) 
#dictionary of currency, stock symbol, exchangeName, instrumentType, firstTradeDate, regularMarketTime, gmtoffset, timezone, exchangeTimeZoneName,
# regularMarketPrice, chartPreviousClose, previousClose, scale, priceHint, currentTradingPeriod (this is its own dictionary)

print(stock.actions) 
#returns quartley dividends + stock splits since stock reached the market

print(stock.dividends) 
#returns quartley dividends since stock reached the market

print(stock.splits) 
#returns stock splits since stock reached the market

print(stock.capital_gains)#seems to work for some mutual funds, return the captial gain

print("Enter multiple stocks:")
stock_name_list = input()

'''