#def RSI(array, period):
#
#  var = array.diff()
#  gain = var.where(var > 0, 0)
#  loss = - var.where(var < 0, 0)
#  avg_gain = gain.rolling(period).mean()
#  avg_loss = loss.rolling(period).mean()
#  rs = avg_gain / avg_loss
#  rsi = 100 - (100 / (1 + rs))
#  
#  return rsi
