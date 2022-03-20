https://www.hackerrank.com/challenges/three-month-preparation-kit-bomber-man/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-seven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def put(grid,b):
    new=[]
    for i in grid:
        line=[]
        for j in i:
            if j=='.':
                line.append(b)
            else:
                line.append(j)
        new.append("".join(line))
    return new

def explore(grid,b):
    new=[]
    n=len(grid)
    m=len(grid[0])
    for i in range(n):
        line=[]
        for j in range(m):
            # check 5 points of possible bomb
            # very long sentence but easy to understand,still more robust
            if grid[i][j] ==b or (i-1>=0 and grid[i-1][j]==b) or (i+1<n and grid[i+1][j]==b) or (j-1>=0 and grid[i][j-1]==b) or (j+1<m and grid[i][j+1]==b):
                line.append('.')
            else:
                line.append(grid[i][j])
        new.append("".join(line))
    return new

def allzero(grid):
    new=[]
    for i in grid:
        line=[]
        for j in i:
            if j!='.':
                line.append('O')
            else:
                line.append('.')
        new.append("".join(line))
    return new

def bomberMan(n, grid):
    # Write your code here
    # loop: 7->3; after -3, 4->0, use (n-3) mod 4
    # 0-7  state
    state=[grid,grid]
    curr=grid
    for i in range(2,7+1):
        equalt=(i-2) % 4
        if equalt==0:
            curr=put(curr,'1')
        elif equalt==1:
            curr=explore(curr,'O')
        elif equalt==2:
            curr=put(curr,'O')
        elif equalt==3:
            curr=explore(curr,'1')
        state.append(curr)
    
    if n<3: # initial state
        # change denotation 1->0
        return allzero(state[n])
    else: # in a circle
        r=(n-3) % 4 + 3
        return allzero(state[r])
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
