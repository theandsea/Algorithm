# https://www.hackerrank.com/challenges/three-month-preparation-kit-jesse-and-cookies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-ten
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq as hp
def cookies(k, A):
    # Write your code here
    hp.heapify(A)
    t=0
    while not (len(A)<=1 or A[0]>=k):
        a=hp.heappop(A)
        b=hp.heappop(A)
        c=a+2*b
        hp.heappush(A,c)
        t +=1
    
    if A[0]>=k:
        return t
    else:
        return -1
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
