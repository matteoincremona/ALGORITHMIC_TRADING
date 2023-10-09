# LOWER Bollinger Band

def BBL(array, period, k):
    """Lower Bollinger Band
    
    Calculate the Lower Bollinger Band of given prices.

    Args:
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the BB calculation (default = 20).
    k (int): The standard deviation (default = 2).
    
    Return (pandas.Series): The values of the Lower BB calculated based on prices, period and sd given.
    """
    
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    
    return BBlow

# MID Bollinger Band

def BBM(array, period, k):
    """Mid Bollinger Band
    
    Calculate the Mid Bollinger Band (mean of the Upper and Lower BBs) of given prices.

    Args:
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the BB calculation (default = 20).
    k (int): The standard deviation (default = 2).
    
    Return (pandas.Series): The values of the Mid BB calculated based on prices, period and sd given.
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    BBmid = (BBup + BBlow) / 2
    
    return BBmid

# UPPER Bollinger Band

def BBU(array, period, k):
    """Upper Bollinger Band
    
    Calculate the Upper Bollinger Band of given prices.

    Args:
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the BB calculation (default = 20).
    k (int): The standard deviation (default = 2).
    
    Return (pandas.Series): The values of the Upper BB calculated based on prices, period and sd given.
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    
    return BBup
