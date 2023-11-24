"""
Que : Given a 2D Matrix filled with integers. Let's say each cell has a weight.
The Top left is (1,1) and bottom right is (N,M) for N - rows, M - columns.
For any location you can move only towards the right or down & can't go outside.
There are two type of queries you need to answer. 1XY & 2XY
Here (X,Y) is the starting location & goal is to reach (N,M).

For type1, you've to collect all weights on your path to (N,M).
For type2, you can decide whether to skip or collect weights 
in any cell on your path.

For both type1 & type2 queries. You've to find what is the maximum sum
of weights that you can collect starting from (X, Y) reaching (N, M).

First line is space separated 2 ints N, M denoting size of matrix.
Each of next N lines contain space separated M ints. Next line is int Q
denothing the number of queries. Next Q lines will have 3 ints
TYPE, start_X, start_Y
Sample I/O:                 Sample O/P:
4 5
-21 1   8   35  40
14  -21 -26 -35 -29
-40 36  48  37  24
46  8   33  -21 -3
4
1   1   1                   114
1   2   2                   121
1   2   4                   23
1   3   5                   21
"""