# https://www.hackerrank.com/challenges/three-month-preparation-kit-torque-and-development/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib<=c_road: # directly bulit for each city
        return n*c_lib
    
    # preparation the connection
    cnn=[[] for i in range(n+1)]
    for [x,y] in cities:
        cnn[x].append(y)
        cnn[y].append(x)
        
    # BFS to traverse
    vist=[False for i in range(n+1)]
    s=0
    for i in range(1,n+1):
        if not vist[i]:
            s += 1 # new part
            q=[i]
            while len(q)>0:
                start=q.pop()
                vist[start]=True
                # add all neighbor to queue
                for ngbr in cnn[start]:
                    if not vist[ngbr]:
                        q.append(ngbr)
    
    # find the minimum cost...built minimum # of library
    mincost=s*c_lib+(n-s)*c_road
    return mincost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
