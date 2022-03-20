# https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    h=0
    pre=0 # previous state
    s = 0
    for ud in path:
        if ud == 'U':
            h += 1
        elif ud == 'D':
            h -= 1
        # now state
        if h>0:
            now=1
        elif h<0:
            now=-1
        elif h==0:
            now=0
        # print(h,now)
        # compare
        if now != pre: # new valley
            if now==-1:
                s += 1
            pre=now
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
