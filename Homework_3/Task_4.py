from forex_python.bitcoin import BtcConverter
from datetime import datetime

year = int(input("Enter the year you bought the bitcoin: "))
month = int(input("Enter the month you bought the bitcoin: "))
day = int(input("Enter the day you bought the bitcoin: "))
paid_usd = float(input("Enter the amount paid for Bitcoin (USD$): "))

bought_date = datetime(year, month, day)
today = datetime.now().date()

btc = BtcConverter()
bought_price = btc.get_previous_price("USD", bought_date)
current_price = btc.get_latest_price("USD")

bitcoin_amount = paid_usd / bought_price
profit = (current_price - bought_price) * bitcoin_amount
if profit >= 0:
    print(f"Your Profit is: {profit:.2f} USD$")
else:
    print(f"Your Loss is: {profit:.2f} USD$")
