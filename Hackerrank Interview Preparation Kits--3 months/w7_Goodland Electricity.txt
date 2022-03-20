# https://www.hackerrank.com/challenges/three-month-preparation-kit-pylons/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-seven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    # using ascending !!!!!!!!!!!!!!!!!!
    num=[]
    # 0-k-1
    for i in range(k):
        if arr[i]==1:
            num.append(1)
        else:
            num.append(0)
    
    index=0 # only ascend and value also optimal in former
    # k-end
    for i in range(k,len(arr)):
        if arr[i]==1:
            while not (arr[index]==1 and i-index<2*k):
                index += 1
            if index==i: # not find
                return -1
            else:
                # print(index,num[index])
                num.append(num[index]+1)
        else:
            num.append(0) 
    
    print(num)
    # min: -(k)-->-1
    index=len(arr)-k
    for i in range(index,len(arr)):
        if arr[i]==1:
            return num[i]
    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
