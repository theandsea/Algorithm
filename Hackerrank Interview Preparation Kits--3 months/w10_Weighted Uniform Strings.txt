# https://www.hackerrank.com/challenges/three-month-preparation-kit-weighted-uniform-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-ten
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    # 1. find the maximum length for each letter
    maxl=[0 for i in range(26+1)]
    pre=''
    leng=0
    w=0
    ord_a=ord('a')
    for ltt in s:
        if ltt==pre:
            leng +=1
        else: # new sequence, reset
            if maxl[w]<leng: # update
                maxl[w]=leng
            # reset
            pre=ltt
            w=ord(ltt)-ord_a+1
            leng=1
    # last one
    if maxl[w]<leng:
        maxl[w]=leng
    
    # 2. for each query, check if divided and within range
    res=[]
    for num in queries:
        find="No"
        for i in range(1,26+1):
            if num % i ==0 and num//i<=maxl[i]:
                find="Yes"
                break
        res.append(find)
        
    return res
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
