# https://www.hackerrank.com/challenges/three-month-preparation-kit-countingsort4/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    count=[[] for i in range(100)]
    n=len(arr)
    half=n//2
    for i in range(n):
        num=int(arr[i][0])
        if i < half:
            string="-"
        else:
            string=arr[i][1]
        count[num].append(string)
    res=[]
    for i in range(len(count)):
        ctlist=count[i]
        for j in range(len(ctlist)):
            res.append(ctlist[j])
    
    resstring=" ".join(res)
    print(resstring)
    return resstring

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
