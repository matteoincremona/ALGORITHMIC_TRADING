def MACD(array, slow_n, fast_n):
  """
  Calculate the Moving Average Convergence Divergence (MACD).
  :param array: The list of the Close prices of the financial instrument.
  :param slow_n: The value of the period for the calculation of the slow moving average (default = 26).
  :param fast_n: The value of the period for the calculation of the fast moving average (default = 12).
  :return: The values of the MACD calculated based on the prices and periods given.
  """
  slow = array.ewm(span = slow_n, adjust = False).mean()
  fast = array.ewm(span = fast_n, adjust = False).mean()
  macd = fast - slow
  
  return macd

# We can also calculate a signal for the MACD, that is a moving average based on the MACD values.

def MACDsignal(macd_values, period):
  """
  Calculate a moving average based on the MACD values and a given period.
  :param macd_values: The values of the MACD of the financial instrument.
  :param period: The value of the period for the calculation of the moving average (default = 9)
  :return: The values of the moving average based on the MACD values and the given period.
  """
  sig = macd_values.ewm(span = period, adjust = False).mean()

  return sig
