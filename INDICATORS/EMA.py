def EMA(array, period):
    """ESPONENTIAL MOVING AVERAGE or ESPONENTIAL WEIGHTED MOVING AVERAGE
    
    Calculate the Esponential Moving Average (EMA), also called Esponential Weighted Moving Average (EWMA).

    Args:
    - array (pandas.Series): The list of the Close prices of the financial instrument.
    - period (int): The period to use for the EMA calculation.
    
    It returns (pandas.Series) the values of the EMA calculated based on the prices and the period given.
    """
    res = array.ewm(span = period, adjust = False).mean()
    
    return res
