from googlefinance import getQuotes
import json

stocks = ["AAPL", "GOOG", "TSLA"]


#Challenge #1

def print_stock_prices():
	stock_data = getQuotes(stocks)
	for stock in stock_data:
		print("{} is trading at ${}".format(stock["StockSymbol"], stock["LastTradePrice"]))

print_stock_prices()


#Challenge #2

def print_stock_lists():
	stock_data = getQuotes(stocks)
	stock_list = []
	
	for item in stock_data:
		stock_list.append([item['StockSymbol'],item['LastTradePrice']])
	
	return(stock_list)		


print(print_stock_lists())


#Challenge #3

def print_stock_dictionaries():
	stock_data = getQuotes(stocks)
	stock_dictionary = []

	for item in stock_data:
		stock_dictionary.append({"Stock":item['StockSymbol'],'Price':item['LastTradePrice']})   

	return(stock_dictionary)

print(print_stock_dictionaries())


















