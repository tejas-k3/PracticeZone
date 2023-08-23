# https://www.hackerrank.com/challenges/sms-splitting/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=hrc-demo
#!/bin/python3
# BUGGY CODE HAS TO CONSIDER WORD CHECK AND WRAP IT UP 
import math
import os
import random
import re
import sys

#
# Complete the 'segments' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

def segments(message):
    msgSize = len(message)
    
    finalMessage = []
    counter = 0
    if msgSize <= 160:
        return [message]
    segments = -(msgSize//-160) 
    print("Length is ", msgSize, " segments are ", segments)
    while counter < segments:
        # NEED TO INTRODUCE A WORD CHECK & PUSH IT TO NEXT SEGMENT :) 
        msg = message[:155]
        msg += f"({counter+1}/{segments})"
        finalMessage.append(msg)
        counter+=1
        message = message[155:]
    return finalMessage

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    result = segments(message)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
