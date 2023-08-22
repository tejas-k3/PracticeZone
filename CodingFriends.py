#!/bin/python3
# https://www.hackerrank.com/challenges/coding-friends/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=hrc-demo
# Did this in too sleepy state zzzzzzz
import math
import os
import random
import re
import sys
import math
#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#

def minNum(samDaily, kellyDaily, difference):
    if (kellyDaily < samDaily or kellyDaily - samDaily == 0 or
    kellyDaily == samDaily and difference > 0):
        return -1
    elif difference + samDaily == kellyDaily:
            return 2
    return math.ceil(difference//(kellyDaily - samDaily)) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samDaily = int(input().strip())

    kellyDaily = int(input().strip())

    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)

    fptr.write(str(result) + '\n')

    fptr.close()
