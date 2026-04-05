import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv('fdata.csv')

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')

# Set index
data.set_index('Date', inplace=True)

# Plot
plt.figure(figsize=(10, 5))

plt.plot(data.index, data['Open'], label='Open')
plt.plot(data.index, data['High'], label='High')
plt.plot(data.index, data['Low'], label='Low')
plt.plot(data.index, data['Close'], label='Close')

plt.title('Alphabet Inc Stock Prices (Oct 3–7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

plt.show()