import yfinance as yf
import sys
import pandas as pd
import numpy as np

def create_ticker(stock_name):
    return yf.Ticker(stock_name)

def print_news_info(stock_name):
    stock = create_ticker(stock_name)
    news_info_list = stock.news
    for article_info_map in news_info_list:
        print("Title: " + article_info_map.get('title'))
    
        print("Link to Article: " + article_info_map.get('link'))
        print()

def ticker_exists(stock_name):
    #Checks if an asset is available via the Yahoo Finance API.
    stock = create_ticker(stock_name)

    info = stock.history(period='7d', interval='1d')
    
    if len(info) <= 0:
        sys.exit("Invalid Stock Name")
    

def stock_value(stock_name):
    #Returns current market value of stock and the sum of n-amount of this stock
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

    
def total_stock_value(curr_value, amount):
    return float(curr_value) * float(amount)


def stock_stats(stock_name):
    stock = create_ticker(stock_name)

    complete_stock_data = stock.info
    stock_info = {}
    
    stock_info["fiftyTwoWeekLow"] = complete_stock_data.get("fiftyTwoWeekLow")
    stock_info["fiftyTwoWeekHigh"] = complete_stock_data.get("fiftyTwoWeekHigh")
    stock_info["52WeekChange"] = complete_stock_data.get("52WeekChange")
    stock_info["previousClose"] = complete_stock_data.get("previousClose")
    stock_info["open"] = complete_stock_data.get("open")
    stock_info["dayLow"] = complete_stock_data.get("dayLow")
    stock_info["dayHigh"] = complete_stock_data.get("dayHigh")
    stock_info["currentPrice"] = complete_stock_data.get("currentPrice")
    stock_info["dividendRate"] = complete_stock_data.get("dividendRate")
    stock_info["dividendYield"] = complete_stock_data.get("dividendYield")
    stock_info["trailingAnnualDividendRate"] = complete_stock_data.get("trailingAnnualDividendRate")
    stock_info["trailingAnnualDividendYield"] = complete_stock_data.get("trailingAnnualDividendYield")

    return stock_info #list with name of stock, open, high, low, close
    
def compare_stocks(stock_list):
    weekLow, weekHigh, weekChange = [], [], []
    prevClose, open, low, high, price = [], [], [], [], []
    dvRate, dvYield, annDvYield, annDvRate = [], [], [], []

    for stock_name in stock_list:
        stock_info = stock_stats(stock_name)
        
        if stock_info.get("fiftyTwoWeekLow") == None: weekLow.append(np.nan)
        else: weekLow.append(stock_info.get("fiftyTwoWeekLow"))

        if stock_info.get("fiftyTwoWeekHigh") == None: weekHigh.append(np.nan)
        else: weekHigh.append(stock_info.get("fiftyTwoWeekHigh"))

        if stock_info.get("52WeekChange") == None: weekChange.append(np.nan)
        else: weekChange.append(stock_info.get("52WeekChange"))
        
        if stock_info.get("previousClose") == None: prevClose.append(np.nan)
        else: prevClose.append(stock_info.get("previousClose"))

        if stock_info.get("open") == None: open.append(np.nan)
        else: open.append(stock_info.get("open"))
        
        if stock_info.get("dayLow") == None: low.append(np.nan)
        else: low.append(stock_info.get("dayLow"))

        if stock_info.get("dayHigh") == None: high.append(np.nan)
        else: high.append(stock_info.get("dayHigh"))

        if stock_info.get("currentPrice") == None: price.append(np.nan)
        else: price.append(stock_info.get("currentPrice"))

        if stock_info.get("dividendRate") == None: dvRate.append(np.nan)
        else: dvRate.append(stock_info.get("dividendRate"))

        if stock_info.get("dividendYield") == None: dvYield.append(np.nan)
        else: dvYield.append(stock_info.get("dividendYield"))

        if stock_info.get("trailingAnnualDividendRate") == None: annDvRate.append(np.nan)
        else: annDvRate.append(stock_info.get("trailingAnnualDividendRate"))

        if stock_info.get("trailingAnnualDividendYield") == None: annDvYield.append(np.nan)
        else: annDvYield.append(stock_info.get("trailingAnnualDividendYield"))

    '''print(len(weekLow))
    print(weekHigh)
    print(weekChange)
    print(len(prevClose))
    print(len(open))
    print(len(low))
    print(len(high))
    print(len(price))
    print(len(dvRate))
    print(len(dvYield))
    print(len(annDvRate))
    print(len(annDvYield))'''

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

    dataFrame = pd.DataFrame(data, index=stock_list)

    #for each stock, call stock_stats and put returned list into conresponding pd.series (name, open, high, low, close)
    print(dataFrame)
    print()
    print(dataFrame.describe())


def db_stock_stats():

    #name of stock, amount of shares, share price, total_stock value
    return 0


def db_compare_stocks(db_list):
    #db_list is list (of tuples) which contains the stock name and share amount

    #for each stock call db_stock_stats and put returned list into corresponding pd.series
    return 0

'''
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