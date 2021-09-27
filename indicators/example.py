import indicators
import yfinance as yf
import matplotlib.pyplot as plt


close_prices = yf.download("BOVA11.SA", "2015-01-02", "2020-07-27")['Close']

ema20 = indicators.ema(20, close_prices.values) # Exponential Moving Average (EMA) of 20 days
ema60 = indicators.ema(60, close_prices.values) # Exponential Moving Average (EMA) of 60 days

plt.plot(close_prices.values, 'b-')
plt.plot(ema20, 'g-', label='EMA 20 days of close prices')
plt.plot(ema60, 'r-', label='EMA 60 days of close prices')
plt.legend()
plt.grid()
plt.show()