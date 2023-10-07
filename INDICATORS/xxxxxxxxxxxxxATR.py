def ATR(High, Low, Close, n):
    """
    Calculate the Average True Range (ATR).
    :param High: The list of the High prices of the financial instrument.
    :param Low: The list of the Low prices of the financial instrument.
    :param Close: The list of the Close prices of the financial instrument.
    :param n: The period to use for the ATR calculation.
    :return: The values of the ATR calculated based on the prices and the period given.
    """
    tr0 = abs(High - Low)
    tr1 = abs(High - Close.shift())
    tr2 = abs(Low - Close.shift())
    db = pd.DataFrame({"tr0": tr0, "tr1": tr1, "tr2": tr2})
    tr = db.max(axis = 1)
    atr = tr.ewm(span = n, adjust = False).mean()
  
    return atr
