def MACD(array, slow_n, fast_n):
  """Moving Average Convergence Divergence
  
  Calculate the Moving Average Convergence Divergence (MACD).

  Args:
  array (pandas.Series): The list of the Close prices of the financial instrument.
  slow_n (int): The value of the period for the calculation of the slow moving average (default = 26).
  fast_n (int): The value of the period for the calculation of the fast moving average (default = 12).
  
  Return (pandas.Series): The values of the MACD calculated based on the prices and periods given.
  """
  slow = array.ewm(span = slow_n, adjust = False).mean()
  fast = array.ewm(span = fast_n, adjust = False).mean()
  macd = fast - slow
  
  return macd

# We can also calculate a signal for the MACD, that is a moving average based on the MACD values.

def MACDsignal(macd_values, period):
  """Moving Average Convergence Divergence Signal

  Calculate a moving average based on the MACD values and a given period.

  Args:
  macd_values (pandas.Series): The values of the MACD of the financial instrument. (see function called "MACD").
  period (int): The value of the period for the calculation of the moving average (default = 9).
  
  Return (pandas.Series): The values of the moving average based on the MACD values and the given period.
  """
  sig = macd_values.ewm(span = period, adjust = False).mean()

  return sig
