def ATR(High, Low, Close, n):
    """AVERAGE TRUE RANGE
    
    Calculate the Average True Range (ATR).

    Args:
    - High (pandas.Series): The list of the High prices of the financial instrument.
    - Low (pandas.Series): The list of the Low prices of the financial instrument.
    - Close (pandas.Series): The list of the Close prices of the financial instrument.
    - n (int): The period to use for the ATR calculation (default = 14).
    
    It returns (pandas.Series) the values of the ATR calculated based on the prices and the period given.
    """
    tr0 = abs(High - Low)
    tr1 = abs(High - Close.shift())
    tr2 = abs(Low - Close.shift())
    db = pd.DataFrame({"tr0": tr0, "tr1": tr1, "tr2": tr2})
    tr = db.max(axis = 1)
    atr = tr.ewm(span = n, adjust = False).mean()
  
    return atr
