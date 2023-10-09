def EMA(array, period):
    """Esponential Moving Average or Esponential Weighted Moving Average
    
    Calculate the Esponential Moving Average (EMA), also called Esponential Weighted Moving Average (EWMA).

    Args:
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the EMA calculation.
    
    Return (pandas.Series): The values of the EMA calculated based on the prices and the period given.
    """
    res = array.ewm(span = period, adjust = False).mean()
    
    return res
