# https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-loss/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    yr=list(range(len(price)))
    zipped=list(zip(price,yr))
    zipped=sorted(zipped,key=lambda x: x[0])
    minx=zipped[-1][0]-zipped[0][0]
    for i in range(len(zipped)-1):
        if zipped[i][1] > zipped[i+1][1]:
            minx =min(minx,zipped[i+1][0]-zipped[i][0])
    return minx
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
