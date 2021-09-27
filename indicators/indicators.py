"""
=========================================
                INDICATORS

                By: Lindtrs

Most of the indicators in this code came
from the book 'Come into my trading room'
written by Dr. Alexander Elder
=========================================
"""

# Simple Moving Average

# n - integer for calculation of the avg. price of n samples (period)
# price - list of prices

def sma (n, price):

  sma = []

  for i in range (0, n-1):

     sma.append(price[0])

  for i in range (n-1 , len(price)):

     summ = 0

     for j in range (0, n):

        summ += price[i-j]

     sma.append(summ/n)

  return sma

#--------------------

# Exponential Moving Average

# n - integer for calculation of the avg. price of n samples (period)
# price - list of prices

def ema (n, price):

  ema = [price[0]]
  k = 2/(n+1)

  for i in range (1, len(price), 1):

     ema.append(price[i] * k + ema[len(ema)-1] * (1-k))

  return ema

#--------------------

# Moving Average Convergence/Divergence

# price - list of close prices

def macd (price):

  ema12 = ema(12, price)
  ema26 = ema(26, price)

  fast_macd = []

  for i in range (0, len(ema12), 1):
  
     fast_macd.append(ema12[i] - ema26[i])

  slow_macd = [] # Slow line or signal line
  slow_macd = ema(9, fast_macd)

  return fast_macd, slow_macd

#--------------------

# Moving Average Convergence/Divergence Histogram

# price - list of close prices


def macd_histogram (price):

  fast_macd , slow_macd = macd(price)

  macd_hist = []

  for i in range (0, len(fast_macd), 1):

     macd_hist.append(fast_macd[i] - slow_macd[i])

  return macd_hist

#--------------------

# Strength Index

# price - list of close prices
# volume - list of traded volume for each price in prices

def strength_index(price, volume):

  strength_index = []

  strength_index.append(0)
  
  for i in range (1, len(price), 1):

     strength_index.append( (price[i] - price[i-1])*volume[i])
  
  strength_index = ema(2, strength_index)

  return strength_index

#--------------------

# Stochastic

# close - list close prices
# high - list of maximum price for each close price
# low - list of minimum price for each close price

def sthocastic (close, high, low):

    #k - fast line
    #d - slow line

    k = []
    d = []

    # For k line
    for i in range (0, len(close), 1):

        k.append( (close[i] - low[i]) / (high[i] - low[i]) * 100 )

    # For d line
    d = sma(3, k)

    return k, d

#--------------------

# Average True Range (ATR)

# close - list close prices
# highs - list of maximums prices
# lows - list of minimums price
# n - integer for calculation of the avg. true range (tr) of n samples (period)

def atr (close, high, low, n=100):

    # high - low
    high_low = [] # High - low
    for i in range (len(close)):
       high_low.append(high[i] - low[i])


    high_prev_close = [0] # High - previous close
    for i in range (1, len(close)):
        high_prev_close.append(high[i] - close[i-1])
    
    low_prev_close = [0] # Low - previous close
    for i in range (1, len(close)):
        low_prev_close.append(low[i] - close[i-1])

    tr = [] # True Range
    for i in range (len(high_low)):
        tr.append( max( high_low[i] , abs(high_prev_close[i]) , abs(low_prev_close[i]) ) )

    atr = ema(n, tr)

    return atr

#--------------------

