def RSI(array, period):
    """RELATIVE STRENGHT INDEX
    
    Calculate the Relative Strenght Index (RSI).
    
    Args:
    - array (pandas.Series): The list of the Close prices of the financial instrument.
    - period (int): The period to use for the RSI (default = 14).
    
    It returns (pandas.Series) the values of the RSI calculated based on the prices and the period given.

    Source: https://www.investopedia.com/terms/r/rsi.asp
    """
  
    var = array.diff()
    gain = var.where(var > 0, 0)
    loss = - var.where(var < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
  
    return rsi
