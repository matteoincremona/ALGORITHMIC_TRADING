from binance import Client
import pandas as pd
import matplotlib.pyplot as plt
import cufflinks as cf

# Set up the personal api keys from Binance

client = Client(api_key, api_secret)

# Getting data (in this example: BTC/USDT, interval = 1 DAY, from 1 Jan 2021 to 31 Dec 2021)

data = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "31 Dec, 2021")

# Creating a dataframe to organize the data

frame = pd.DataFrame(data)
frame = frame.iloc[:,:5]
frame.columns = ["Date", "Open", "High", "Low", "Close"]
frame = frame.set_index("Date")
frame.index = pd.to_datetime(frame.index, unit = "ms")
frame = frame.astype(float)
del frame["High"]
del frame["Low"]
frame["DeltaPerc"]= frame.Close.pct_change() # delta % (close(n - 1) - close(n))

# For this strategy, I will use 3 EMA

def EMA(array, period):
    
    esp = array.ewm(span = period, adjust = False).mean()
    
    return esp

frame["EMA5"] = EMA(frame.Close, 5)
frame["EMA10"] = EMA(frame.Close, 10)
frame["EMA20"] = EMA(frame.Close, 20)

frame = frame.assign(Position = 1)
frame = frame.astype(float)

# ------------- STRATEGY -------------
# OPEN LONG --> if EMA5 > EMA 10 and EMA5 > EMA20
# CLOSE LONGE if EMA5 < EMA10 or EMA5 < EMA20

for i in range(0, len(frame)):
    
    if frame.EMA5[i] > frame.EMA10[i] and frame.EMA5[i] > frame.EMA20[i]:
        frame.Position[i] = frame.Position[i] * 1
        
    else:
        frame.Position[i] = frame.Position[i] * 0

frame.Position = frame.Position.shift(1)

# --------------------------

frame = frame.assign(Return = 1)
frame = frame.astype(float)

for i in range(0, len(frame)):
    
    frame.Return[i] = frame.DeltaPerc[i] * frame.Position[i]  

frame["Cum_Return"] = (frame.Return + 1).cumprod() * 100 # Cum Return
frame["BuyHold"] = (frame.DeltaPerc + 1).cumprod() * 100 # BuyHold %
frame["Counter"] = ""

for i in range(0, len(frame)):
    
    if (frame.Position[i] == 1 and frame.Position[i-1] == 0):
        frame.Counter[i] = "Open_L"
        
    elif (frame.Position[i] == 0 and frame.Position[i-1] == 1):
        frame.Counter[i] = "Close_L"

# Interactive ASSET and P/L visualization

cf.go_offline() # will make cufflinks offline
cf.set_config_file(offline = False, world_readable = True)
frame[["Close", "EMA5", "EMA10", "EMA20"]].iplot()
frame.Cum_Return.iplot(kind = "line", color = "green", theme = "white", title = "P/L", xTitle = "Time", yTitle = "%")

# Summary of the stategy:

Open_positions = 0
Closed_positions = 0


for i in range(0, len(frame)):
    
    if frame.Counter[i] == "Open_L":
        Open_positions = Open_positions + 1
    
    elif frame.Counter[i] == "Close_L":
        Closed_positions = Closed_positions + 1

print("\n------- STRATEGY SUMMARY -------\n")
print("Total days             ", len(frame))
print("Total months           ", (len(frame))/30)
print("Total years            ", (len(frame))/365)
print("# OPENED positions     ", Open_positions)
print("# CLOSED positions     ", Closed_positions)
print("P/L [%]                ", frame.Cum_Return[-1] - 100)
print("BuyHold [%]            ", frame.BuyHold[-1] - 100)
print("Max Drowdown [%]       ", frame.Cum_Return.min() - 100)
print("Max Profit [%]         ", frame.Cum_Return.max() - 100)


