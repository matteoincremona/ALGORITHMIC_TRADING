def SMA(array, period):
    """Single Moving Avergae
    
    Calculate the Single Moving Average (SMA) of given prices.

    Args
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the SMA calculation.
    
    Return: The values of the SMA calculated based on the prices and the period given.
    """
    
    return array.rolling(period).mean()
