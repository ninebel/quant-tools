import yfinance as yf
import matplotlib.pyplot as plt
from macd_divergence import macd_divergence
    
prices = yf.download("BIDI4.SA", start="2021-01-01", end="2021-05-30", interval="1d")['Close']

macd_h = macd_histogram(prices) # DO NOT FORGET TO IMPORT MACD_HISTOGRAM FROM THE INDICATORS!!

operation = macd_divergence(prices, macd_h)

print('Op. code:', operation)

if operation == 0:
    print('Neutral')
elif operation == 1:
    print('Buy')
elif operation == -1:
    print('Sell')
elif operation == None:
    print('Error')



