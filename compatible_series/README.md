# CompatibleSeries

This program's may purpose is to find compatible series of points in a database, and then output the compatible series found.

## Example

If you want to search in a database A for the points in a list B, assuming:

X points of A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <br>
Y points of A = [6, 7, 8, 6, 7, 6, 5, 4, 3, 2] <br>
B = [6, 7] 

Attention: B only has the Y points we  will be searching for

The program will return 2 series, which X points are [0, 1] and [3, 4], so this means that the values of Y points of A, located on the X points of each serie will contain the points we are searching for.

X | Y <br>
*0* | *6* <br>
*1* | *7* <br>
2 | 8 <br>
*3* | *6* <br>
*4* | *7* <br>
5 | 6 <br>
6 | 5 <br>
7 | 4 <br>
8 | 3 <br>
9 | 2 <br>

So, at the table above each, we can confirm the program found the points we were looking for, the first serie of points was found in X=0 and X=1, matching the Y=6 and Y=7, and the second serie was found in X=3 and X=4, matching the Y=6 and Y=7 (B list we were searching).

Note: For a more professional Technical Analysis Library, you can use TA-Lib and its python wrapper (https://github.com/mrjbq7/ta-lib)
