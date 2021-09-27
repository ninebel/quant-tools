
import compatible_series

# dataY - list of the data points you want to find

# datasetX - list of X points of your search dataset

# datasetY - list of Y points of your search dataset

# margin - int or float of max. error between your search point and a dataset point
# Example: If it is 5%, and your search point is 10, then every point between 9.5 and 10.5 will be valid

# wrongPointsPercentage - int or float of max. tolerance to wrong points in a serie
# Example: If it is 25%, and your dataY has 4 points, this means one point can be wrong, if the other 3 are compatible, then the serie is valid

dataset_x = [1, 2,  3, 4, 5, 6,  7,   8,  9, 10, 11, 12, 13] # List with dataset points X

dataset_y = [2, 4, 20, 8, 4, 6, 8.2, 10, 12, 14, 16, 18, 20] # List with dataset points Y

# Note: dataset_x must be the same size as dataset_y!

data_y = [4.1, 6, 8.4] # Data we will be searching for 

series_x, series_y = compatible_series.scan(data_y, dataset_x, dataset_y, margin=5, wrong_points_percentage=25)

print(len(series_x), "series found!")

print("Series of X points:", series_x)

print("Series of Y points:", series_y)

# Expected output:  X = [2, 3, 4], [5, 6, 7] (2 series)  Y = [4, 20, 8], [4, 6, 8.2] (2 series)
# The point 8.2 was accepted as valid because of margin tolerance, in a similar way the point 20 was much higher than tolerated by margin, but it was also considered valid because of wrong_points_percentage

