def RSI(array, period):
    """Relative Strenght Index
    
    Calculate the Relative Strenght Index (RSI).
    
    Args:
    array (pandas.Series): The list of the Close prices of the financial instrument.
    period (int): The period to use for the RSI (default = 14).
    
    Return(pandas.Series): The values of the RSI calculated based on the prices and the period given.
    """
  
    var = array.diff()
    gain = var.where(var > 0, 0)
    loss = - var.where(var < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
  
    return rsi
