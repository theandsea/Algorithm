# https://www.hackerrank.com/challenges/three-month-preparation-kit-chief-hopper/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    # by a polynomial operation
    # a[k]=2*a[k-1]-h[k] --> atimes(t), num(constant, c)
    # but this might be exponential and overflow
    # we can also use binary search since it is ascending structure
    maxx=100000
    for i in range(1,maxx+1):
        curr=i
        find=True
        for h in arr:
            curr += curr-h
            if curr < 0 :
                find=False
                break
            elif curr >maxx: # definitely go through all the rest
                return i
        if find: # go through all height
            return i
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
