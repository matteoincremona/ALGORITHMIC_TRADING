def SMA(array, period):
    """SINGLE MOVING AVERAGE
    
    Calculate the Single Moving Average (SMA) of given prices.

    Args:
    - array (pandas.Series): The list of the Close prices of the financial instrument.
    - period (int): The period to use for the SMA calculation.
    
    It returns (pandas.Series) the values of the SMA calculated based on the prices and the period given.

    Source: https://www.investopedia.com/terms/m/movingaverage.asp
    """
    
    return array.rolling(period).mean()
