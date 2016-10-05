from flask import Flask, render_template, request
import os
import weather
from googlefinance import getQuotes
app = Flask(__name__)



def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]['LastTradePrice']
    return "The price of {} is {}".format(ticker, price)



@app.route('/')
def index():
    name = request.values.get('name', 'Nobody') #will return 'Nobody' is no name is provided
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)



@app.route("/about")
def about():
	return render_template('about.html')



@app.route('/results')
def results():
    stock = request.values.get('stock')
    price = get_stock_price(stock)
    return render_template('results.html', price=price)



if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)



# @app.route("/old_index")
# def old_index():
# 	address = request.values.get('address')
# 	forecast = None
# 	if address:
# 		forecast = weather.get_weather(address)
# 	return render_template('old_index.html', forecast=forecast)


#app.run(debug=true)

# @app.route('/in/<username>')
# def profile():
#     user = get_user(username)
#     return render_template('profile.html', user=user)

