# https://www.hackerrank.com/challenges/three-month-preparation-kit-sum-vs-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    # only x*y<=x+y  "="  (0,1) or (0,1) or (0,0) have same result
    curr=n
    b=[] # from low to high
    while curr >0:
        b.append(curr % 2)
        curr //= 2
    
    # 0->0,1; 1->0
    s = 1
    for i in reversed(range(len(b))): # from high to low
        if b[i]==0:
            s *=2
    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
