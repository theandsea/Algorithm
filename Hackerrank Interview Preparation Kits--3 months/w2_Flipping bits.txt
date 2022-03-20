# https://www.hackerrank.com/challenges/three-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    # 1. convert to 2-bits
    curr = n
    bits=[]
    while curr>0: # from low to high
        bits.append(curr % 2)
        curr //= 2
    for i in range(32-len(bits)):
        bits.append(0)
    
    # 2. flip
    for i in range(len(bits)):
        bits[i] = 1- bits[i]
    
    # 3. convert to integer
    # from high to low
    s = 0
    for i in reversed(range(len(bits))):
        s *= 2
        s += bits[i]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
