# https://www.hackerrank.com/challenges/three-month-preparation-kit-lilys-homework/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eleven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def single(arr,correct):
    dic={}
    for i in range(len(correct)):
        dic[correct[i]]=i
    
    # 2.loop to find the number of circle
    s=0
    n=len(arr)
    vist=[False for i in range(len(arr))]
    for i in range(len(arr)):
        # not visited, not single points(actually doesn't matter)
        if (not vist[i]):#  and (i != dic[arr[i]]):
            t=-1
            curr=i
            while not vist[i]:
                vist[i]=True
                i=dic[arr[i]]
                t += 1
            s += t
    
    return s
    # 3.res= # of disorder - # of circle

import copy
def lilysHomework(arr):
    # Write your code here
    # 1.quick sort to find the correct order
    correct=sorted(arr,key=lambda x:x)
    
    # 2 option: min order or reversed order
    reverted=copy.copy(correct)
    reverted.reverse()
    return min(single(arr,correct),single(arr,reverted))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
