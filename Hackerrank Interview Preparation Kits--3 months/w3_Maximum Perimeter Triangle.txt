# https://www.hackerrank.com/challenges/three-month-preparation-kit-maximum-perimeter-triangle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # since n is small, use brutal force
    sticks.sort() # still judge according to the order
    most=-1
    side=[]
    n=len(sticks)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if sticks[i]<sticks[j]+sticks[k] and sticks[i]>abs(sticks[j]-sticks[k]):
                    if most < sticks[i]+sticks[j]+sticks[k]:
                        side=[sticks[i],sticks[j],sticks[k]]
                        most=sticks[i]+sticks[j]+sticks[k]
    if most==-1:
        return [-1]
    else:
        return side

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
