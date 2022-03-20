# https://www.hackerrank.com/challenges/three-month-preparation-kit-cube-summation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cubeSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY operations
#

def cubeSum(n, operations):
    # Write your code here
    # no need to use segment tree, since m are relatively small
    # update != sum up
    # directly sum up all fit value
    res=[]
    # points=[[[0 for k in range(n+1)]for j in range(n+1)] for i in range(n+1)]
    points={}
    sups=0
    for cmd in operations:
        para=cmd.split(" ")
        if para[0]=="UPDATE":
            x=int(para[1])
            y=int(para[2])
            z=int(para[3])
            W=int(para[4])
            # points[x][y][z] += W
            points[(x,y,z)]=W
            # sups += W
            # print(sups)
        elif para[0]=="QUERY":
            x1=int(para[1])
            y1=int(para[2])
            z1=int(para[3])
            x2=int(para[4])
            y2=int(para[5])
            z2=int(para[6])
            s=0
            for (x,y,z) in points:
                if x1<=x and x<=x2 and y1<=y and y<=y2 and z1<=z and z<=z2:
                    s += points[(x,y,z)]
            res.append(s)
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        matSize = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        ops = []

        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)

        res = cubeSum(matSize, ops)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

    fptr.close()
