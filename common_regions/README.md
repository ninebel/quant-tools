# CommonRegions
Search for a region with common points (basically finds common Y values that are close to each other in a sequence)

## Example

We want to find regions that have points in common, assuming our search database is a list with 10 values: [0, 1, 2.1, 2, 3, 4, 5, 6, 6, 6] (Y values) <br>

When we run the program with margin=5 and minPointsPercentage=20, it will output 2 regions, [2.05, 6.0], this means there will be a region with close or identical points when Y=2.05 and Y=6. <br>
The minimum numbers of points to have a region is: number of values X (minPointsPercentage/100), in this case, 10 X 0.2 = 2, if we have two identical or close points, it will be considered as a region, 2.1 was considered a similar point to 2 beucase we have a 5% margin (5% of 2 is 0.1). So, 2.05 and 6 are regions, as they have 2 or more identical/close points, 2.05 is the average of his two points (2 and 2.1). <br>

## Applications

I have used this program to find resistance and support regions in stock charts. The file Example2.py in the root directory has an example of its application using yahoo finance and matplotlib libraries.
