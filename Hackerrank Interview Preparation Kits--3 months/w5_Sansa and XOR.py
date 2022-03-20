# https://www.hackerrank.com/challenges/three-month-preparation-kit-sansa-and-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
    # communicative & associative...compute the number
    n=len(arr)
    # A*A=0; 0*A=0 ===> only odd or even affects...zig,zag; ab==>(a+1)*(b-1)
    if n % 2 ==0:
        times=[0 for i in range(n)] # 0^0...^0=0 even
        return 0
    else:
        times=[(i+1)%2 for i in range(n)]
        res=0
        for i in range(n):
            if times[i]==1:
                res ^= arr[i]
        return res
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
