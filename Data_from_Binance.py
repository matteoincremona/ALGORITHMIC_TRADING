# This is how I get and how I manage data from Binance
# (I am using API and not the Websocket beacuse (personally) I don't need a continuous comunication with Binance)

from binance import Client
import pandas as pd
import matplotlib.pyplot as plt

client = Client(api_key, api_secret)

# Getting data:

data = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "21 Feb, 2022", "20 Feb, 2023")
# data = client.get_historical_klines("ETHBUSD", Client.KLINE_INTERVAL_1DAY, "21 Feb, 2022")
# data = client.get_historical_klines("BTCETH", Client.KLINE_INTERVAL_1DAY, "1 day ago UTC") # up to now

data = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "31 Dec, 2021")

# Organizing data:

frame = pd.DataFrame(data)
frame = frame.iloc[:,:5]
frame.columns = ["Date", "Open", "High", "Low", "Close"]
frame = frame.set_index("Date")
frame.index = pd.to_datetime(frame.index, unit = "ms")
frame = frame.astype(float)

