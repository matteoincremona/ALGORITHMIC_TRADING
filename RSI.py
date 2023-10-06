import pandas as pd
import numpy as np

# Load the data into a Pandas dataframe
df = pd.read_csv('data.csv')

# Calculate the price change for each period
delta = df['Close'].diff()

# Define the period for the rolling average
period = 14

# Calculate the average gain and average loss for the specified period
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(period).mean()
avg_loss = loss.rolling(period).mean()

# Calculate the Relative Strength (RS) by dividing the average gain by the average loss
rs = avg_gain / avg_loss

# Calculate the Relative Strength Index (RSI)
rsi = 100 - (100 / (1 + rs))

# Add the RSI to the dataframe
df['RSI'] = rsi

# Print the dataframe
print(df.head())


def RSI(array, period):

  var = 
