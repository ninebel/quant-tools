"""

MACD Strategy

prices - list (array) with prices
macd_histogram - list (array) with MACD histogram of prices

Return 0 means NEUTRAL
Return -1 means SELL
Return 1 means BUY
Return None means ERROR

"""

def macd_divergence (prices, macd_histogram):

    # Parameters
    max_samples = 500 # This may not be bigger than the data size!
    n_maxs_mins = 3
    max_age = 1


    prices = list(prices) # Convert any type of array data to default python array/list!
    macd_histogram = list(macd_histogram)

    # If one lists has more data than another (unbalanced), do nothing!
    if len(prices) != len(macd_histogram):

        print('Lists prices and macs_histogram are not the same size!')
        return None

    # If theres too much data, use only the last 500 samples/candles!
    if len(prices) > 500:
        
        prices = prices[ len(prices)-max_samples : len(prices) ]
        macd_histogram = macd_histogram[ len(macd_histogram)-max_samples : len(macd_histogram) ]


    # FIND MAXIMUM AND MINIMUM VALUES IN MACD HISTOGRAM

    divisions = [] # List with the intervals between maximums and minimums (x axis - time)
    for i in range (len(prices)-1, -1, -1): # Iterates from last value to the first one!

        # If the current value is greater than zero AND the last value is less than 0
        # OR
        # If the current value is less than zero AND the last value is greater than 0
        if (macd_histogram[i] > 0 and macd_histogram[i-1] < 0) or (macd_histogram[i] < 0 and macd_histogram[i-1] > 0):

            divisions.append(i)

        # If all necessary divisions were found
        if len(divisions) == n_maxs_mins+1: 
            break

    # If there is the right number of divisions
    if len(divisions) != n_maxs_mins+1:
        print("Error when finding the necessary divisions between max/min intervals!")
        return None

    divisions.reverse() # Reverse the division, because it goes from big values to small ones, we need the opposite for the limits

    # Scan for maximum and minimum values in the intervals delimited by divisions for MACD Histogram
    macd_max_min_x = []
    macd_max_min_y = []
    for i in range (0, len(divisions)-1, 1):

        lower_limit = divisions[i]
        upper_limit = divisions[i+1]
        macd_histogram_interval = macd_histogram[ lower_limit : upper_limit ]
        max_value = max( macd_histogram_interval )
        min_value = min( macd_histogram_interval )

        # If there are repeated values!
        if macd_histogram_interval.count(max_value) != 1 or macd_histogram_interval.count(min_value) != 1:
            print('There are two or more max/min values in an interval!')
            return None

        if max_value >= abs(min_value): # Maximum value
            macd_max_min_y.append(max_value)
            macd_max_min_x.append( lower_limit + macd_histogram_interval.index(max_value) )
            #print(macd_max_min_x[-1])

        elif max_value <= abs(min_value): # Minimum value
            macd_max_min_y.append(min_value)
            macd_max_min_x.append( lower_limit + macd_histogram_interval.index(min_value) )
            #print(macd_max_min_x[-1])

    #print('-0------------')
    # STRATEGY
    #return macd_max_min_x

    if len(prices) - divisions[-1] <= max_age: # If the signal is not older than 5 candles!

        # High Divergence (BUY 1)
        if prices[ macd_max_min_x[1] ] < prices[ macd_max_min_x[0] ] and macd_max_min_y[2] > macd_max_min_y[0]:
            return 1
    
        # Low Divergence (SELL -1)
        elif prices[ macd_max_min_x[1] ] > prices[ macd_max_min_x[0] ] and macd_max_min_y[2] < macd_max_min_y[0]:
            return -1

        # Neutral (0)
        else:
            return 0

    # Neutral (0)
    else:
        return 0
