# https://www.hackerrank.com/challenges/three-month-preparation-kit-queries-with-fixed-length/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eleven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    n=len(arr)
    res=[]
    for d in queries:
        curr=max(arr[:d])
        nowmin=curr
        for i in range(1,n-d+1):
            new=arr[i+d-1]
            if new>=curr:
                curr=new
            elif new<curr and arr[i-1]==curr: # the lost one
                curr=max(arr[i:i+d])
                if nowmin > curr:
                    nowmin = curr
            # print(new,curr,arr[i-1],nowmin)
        # print("=================")
        res.append(nowmin)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
