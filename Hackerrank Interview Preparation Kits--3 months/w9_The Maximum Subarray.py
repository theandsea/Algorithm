# https://www.hackerrank.com/challenges/three-month-preparation-kit-maxsubarray/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    # subarray--dp
    arr_s=0
    subarr=[0 for i in range(len(arr))] # the maximum sum of subarray ending(include) at that point
    subarr[0]=arr[0]
    for i in range(1,len(arr)):
        # 2 choice, start a new subarray, or continue the subarray
        itself=arr[i]
        if subarr[i-1] >0: # continue
            subarr[i]=subarr[i-1] + itself
        else:
            subarr[i]=itself
        
    arr_s=max(subarr)
        
    # subsequence--all the positive
    seq_s=0
    for num in arr:
        if num>0:
            seq_s += num
            
    # maybe all negative
    if seq_s==0:
        seq_s=max(arr)
    return [arr_s,seq_s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
