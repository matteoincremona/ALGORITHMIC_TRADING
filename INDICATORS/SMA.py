def SMA(array, period):
    """
    Calculate the Single Moving Average (SMA) of given prices.
    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the SMA calculation.
    :return: The values of the SMA calculated based on the prices and the period given.
    
    """
    
    return array.rolling(period).mean()
