import common_regions

# data - list of database points the program will scan to find the regions

# margin - int or float of max. error between two points to be considered similar

# minPointsPercentage - int or float of the minimum percentage of close/identical points a region must have to be considered a region

data = [0, 1, 2.1, 2, 3, 4, 5, 6, 6, 6]

regions = common_regions.scan(data, margin=5, minPointsPercentage=20)

print("Found", len(regions), "regions")
print(regions)

# Expected output: [2.05, 6.0] (2 regions)
# In this case, to be considered a region it must have at least 2 close/identical points ( len(data) * (minPointsPercentage/100) -> 10 x 0.2 = 2)
# 2.1 is considered a similar point to 2 because we set a 5% margin (5% of 2 is 0.1)


