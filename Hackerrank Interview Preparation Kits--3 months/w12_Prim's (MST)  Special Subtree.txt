# https://www.hackerrank.com/challenges/three-month-preparation-kit-primsmstsub/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#
import heapq as hp
def prims(n, edges, start):
    # Write your code here
    # similar to Dijkstra, only no accumulated cost
    # or just find the non-overlaped edges..but must use Union Find to test connection
    cnn=[[] for i in range(n+1)]
    for [a,b,w] in edges:
        cnn[a].append((b,w))
        cnn[b].append((a,w))
    print(cnn)
        
    vist=[False for i in range(n+1)]
    A=[(0,start)] # w, point
    total=0
    s = 0
    while len(A)>0 and s<n:
        (w,p)=hp.heappop(A)
        if not vist[p]: # totally determined
            vist[p]=True
            total += w
            s += 1
            # print(w,p)
            # expand all its neighbor
            for (ngb,cost) in cnn[p]:
                if not vist[ngb]:
                    hp.heappush(A,(cost,ngb))
            # print(A)
    if s==n: # find all
        return total
    else:
        return -1                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
