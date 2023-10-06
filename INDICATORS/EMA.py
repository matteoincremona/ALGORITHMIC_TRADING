def EMA(array, period):
    """
    Calculate the Esponential Moving Average (EMA), also called Esponential Weighted Moving Average (EWMA).
    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the EMA calculation.
    :return: The values of the EMA calculated based on the prices and the period given.
    
    """
    res = array.ewm(span = period, adjust = False).mean()
    
    return res
