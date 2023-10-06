#def ATR(High, Low, Close, n):
#
#    tr0 = abs(High - Low)
#    tr1 = abs(High - Close.shift())
#    tr2 = abs(Low - Close.shift())
#    tr = [tr0, tr1, tr2].max(axis = 1)
#    ema = values.ewm(span = n, adjust = False).mean()
#    atr = ema(tr, n)
#  
#    return atr
