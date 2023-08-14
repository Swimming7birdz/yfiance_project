import yfinance as yf
import sys

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
    

def stock_value(stock_name, amount):
    #Returns current market value of stock and the sum of n-amount of this stock
    stock = create_ticker(stock_name)

    #need to return price at closing when markets are closed

    try:
        data = stock.history(period="1d", interval="1m")
        curr_value = data["Close"].iloc[-1]
        #returns accurate price when markets are up
        #returns stock price 2-5 minutes before markets closed 

        total_value = float(curr_value) * float(amount)

        print(stock_name)
        print("Current Stock Price: " + str(curr_value))
        print()
        print("Total Stock value: " + str(total_value))

    except IndexError:
        sys.exit("Error occurred, terminating stock value calculation")

    



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