# https://www.hackerrank.com/challenges/three-month-preparation-kit-journey-to-the-moon/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    # again try to traverse and find the number of each connected part
    # preparation--cnn[x]...x's neighbor(same country)
    cnn=[[] for i in range(n)]
    for [x,y] in astronaut:
        cnn[x].append(y)
        cnn[y].append(x)
    # print(cnn)
        
    # BFS to traverse, get the # of each group: group[]
    # where to change the vist?????? in case other branch expand the same points
    group=[]
    vist=[False for i in range(n)]
    for i in range(n):
        if not vist[i]: # not visited
            st=[i]
            # print(st)
            vist[i]=True
            s=1 # #of this group
            while len(st)>0:
                start=st.pop()
                # add all its neighbor
                for ngbr in cnn[start]:
                    if not vist[ngbr]: 
                        vist[ngbr]=True # in case other branch expand the same points
                        st.append(ngbr)
                        s += 1
                # print(st)
            group.append(s)
    # print(group)
    
    # choose from group A and other groups(by presum), and sum all possible group A
    # to avoid repeated, only jointed with the groups with index < index_A
    s = 0
    presum=[]
    for i in range(len(group)):
        s += group[i]
        presum.append(s)
    
    s = 0
    for i in reversed(range(1,len(group))):
        s += group[i]*presum[i-1]    
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
