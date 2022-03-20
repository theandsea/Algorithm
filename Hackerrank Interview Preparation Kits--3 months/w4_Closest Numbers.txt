# https://www.hackerrank.com/challenges/three-month-preparation-kit-closest-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    n=len(arr)
    mindiff=arr[-1]-arr[0]
    for i in range(n-1):
        if mindiff > arr[i+1]-arr[i]:
            mindiff = arr[i+1]-arr[i]
    
    res=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]-arr[i] == mindiff:
                res.append(arr[i])
                res.append(arr[j])
            else:
                break
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
