def EMA(array, period):
    
    res = array.ewm(span = period, adjust = False).mean()
    
    return res
