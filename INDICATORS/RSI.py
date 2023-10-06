def RSI(array, period):
    """
    Calculate the Relative Strenght Index (RSI).

    :param array: The list of the Close prices of the financial instrument.
    :param period: The period to use for the RSI (default = 14).
    :return: The values of the RSI calculated based on the prices and the period given.
  
    """
  
    var = array.diff()
    gain = var.where(var > 0, 0)
    loss = - var.where(var < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
  
    return rsi
