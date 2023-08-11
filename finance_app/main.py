import yfinance as yf

def print_news_info(news_info_list):
    for article_info_map in news_info_list:
        print("Title: " + article_info_map.get('title'))
    
        print("Link to Article: " + article_info_map.get('link'))
        print()




#print("Enter a stock:")
#stock_name = input()
stock_name = "AAPL"

stock = yf.Ticker(stock_name)

print(len(stock.news))
print_news_info(stock.news)

#print_news_info(stock.news())
#print(stock.info)

'''
print("Enter multiple stocks:")
stock_name_list = input()V

'''