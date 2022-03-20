# https://www.hackerrank.com/challenges/three-month-preparation-kit-lego-blocks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-ten
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod=1000000007
    # 1. single layer
    sgl=[1,1,2,4] # next is 4
    for i in range(4,m+1):
        num=(sgl[i-1]+sgl[i-2]+sgl[i-3]+sgl[i-4]) % mod
        sgl.append(num)
    
    # 2. multi layer
    multi=[]
    for single in sgl:
        total=1
        for i in range(n):
            total = total * single % mod
        multi.append(total)
        
    # 3. multi layer without seam
    # class as: seam at 1,2 ... i-1 + no seam
    noseam=[1]
    for i in range(1,m+1): # i is length
        total=multi[i]
        for j in range(1,i):
            # seam at j ==> noseam[j]*multi[i-j]
            total = (total-noseam[j]*multi[i-j])%mod
            # total %=mod
        noseam.append(total)
    
    # last total
    return (total+mod) % mod
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
