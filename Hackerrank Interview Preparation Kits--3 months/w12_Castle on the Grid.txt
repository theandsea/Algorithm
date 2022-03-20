# https://www.hackerrank.com/challenges/three-month-preparation-kit-castle-on-the-grid/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    # equal cost for each step, BFS
    n=len(grid)
    vist=[[-1 for j in range(n)]for i in range(n)]
    vist[startX][startY]=0
    
    # BFS
    que=[(startX,startY,0)]
    f=0
    while f<len(que):
        x,y,cost=que[f]
        f += 1
        if f==10000:
            que=que[10000:]
            f=0
        # expand
        # up (-1,)
        newx=x-1
        while newx>=0 and grid[newx][y]!='X':
            if vist[newx][y]==-1:
                vist[newx][y]=cost+1
                que.append((newx,y,cost+1))
            newx -=1
        # down (+1,)
        newx=x+1
        while newx<n and grid[newx][y]!='X':
            if vist[newx][y]==-1:
                vist[newx][y]=cost+1
                que.append((newx,y,cost+1))
            newx +=1
        # left (,-1)
        newy=y-1
        while newy>=0 and grid[x][newy]!='X':
            if vist[x][newy]==-1:
                vist[x][newy]=cost+1
                que.append((x,newy,cost+1))
            newy -=1
        # right (,+1)newy=y-1
        newy=y+1
        while newy<n and grid[x][newy]!='X':
            if vist[x][newy]==-1:
                vist[x][newy]=cost+1
                que.append((x,newy,cost+1))
            newy +=1
        # check result
        if vist[goalX][goalY] !=-1:
            return vist[goalX][goalY]
    
    # not found
    return -1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
