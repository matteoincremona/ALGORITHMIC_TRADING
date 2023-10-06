# LOWER Bollinger Band

def BBL(array, period, k):
    """
    Calculate the Lower Bollinger Band of given prices.
    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the BB calculation.
    :param k: The standard deviation.
    :return: The values of the Lower BB calculated based on prices, period and sd given.
    """
    
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    
    return BBlow

# MID Bollinger Band

def BBM(array, period, k):
    """
    Calculate the Mid Bollinger Band (mean of the Upper and Lower BBs) of given prices.
    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the BB calculation.
    :param k: The standard deviation.
    :return: The values of the Mid BB calculated based on prices, period and sd given.
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    BBmid = (BBup + BBlow) / 2
    
    return BBmid

# UPPER Bollinger Band

def BBU(array, period, k):
    """
    Calculate the Upper Bollinger Band of given prices.
    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the BB calculation.
    :param k: The standard deviation.
    :return: The values of the Upper BB calculated based on prices, period and sd given.
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    
    return BBup
