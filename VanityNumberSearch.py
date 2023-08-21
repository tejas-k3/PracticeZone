#!/bin/python3
# https://www.hackerrank.com/challenges/vanity-number-search/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=hrc-demo
import math
import os
import random
import re
import sys

#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

def vanity(codes, numbers):
    numMap = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9',
        ' ': '0'
    }
    def convertToNum(code):
        num = ""
        for char in code:
            num+=numMap[char.lower()]
        return num
    numbers = list(set(numbers))
    res= []
    for code in codes:
        code = convertToNum(code)
        for number in numbers:
            if code in number:
                res.append(number)
    res.sort()
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    codes_count = int(input().strip())

    codes = []

    for _ in range(codes_count):
        codes_item = input()
        codes.append(codes_item)

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = input()
        numbers.append(numbers_item)

    result = vanity(codes, numbers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
