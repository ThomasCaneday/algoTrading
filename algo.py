import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("NVDA", start="2020-01-01", end="2024-10-01")

data["Close"].plot(title="Nvidia Closing Prices")
plt.show()

data['SMA10'] = data['Close'].rolling(window=10).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()
