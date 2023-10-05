def BBL(array, period, k):
    
    BB1 = SMA(array, period) - k * array.rolling(period).std()
    
    return BB1

def BBU(array, period, k):
    
    BB2 = SMA(array, period) + k * array.rolling(period).std()
    
    return BB2
