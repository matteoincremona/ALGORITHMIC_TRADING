def SMA(array, period):
    
    return array.rolling(period).mean()
