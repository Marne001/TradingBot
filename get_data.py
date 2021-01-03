import csv
import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

candles = client.get_klines(symbol='ZILUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2012-2020.csv', 'w', newline='')
candlestickwriter = csv.writer(csvfile, delimiter=',',)

#for candlestick in candles:
    #print(candlestick)

    #candlestickwriter.writerow(candlestick)

#print(len(candles))

candlesticks = client.get_historical_klines("ZILUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "24 May, 2020")

for candlestick in candlesticks:
    candlestickwriter.writerow(candlestick)

csvfile.close()

