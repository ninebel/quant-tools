import common_regions
import yfinance as yf
import matplotlib.pyplot as plt

close_prices = yf.download("BOVA11.SA", "2010-01-02", "2020-07-27")['Close'] # This is a dataframe

regions = common_regions.scan(close_prices.values, margin=15, minPointsPercentage=2)
print('Number of regions found:', len(regions))

plt.plot(close_prices.values, 'b-')

for i in range (0, len(regions), 1):
    aux = []
    for j in range (len(close_prices.values)):

        aux.append(regions[i])

    plt.plot(aux, 'r-')

plt.show()


