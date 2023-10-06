def EMA(array, period):
    
    res = array.ewm(span = period, adjust = False).mean()
    # alpha = 1/n --> see on tradingview which if the values are correct
    return res
