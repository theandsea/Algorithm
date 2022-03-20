# https://www.hackerrank.com/challenges/three-month-preparation-kit-climbing-the-leaderboard/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-seven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # Write your code here
    # ranked, player already sorted !!!!!!
    # using ascending !!!
    ranked.sort()
    ranked.reverse()
    # remove the same
    newrank=[]
    pre=-1
    for num in ranked:
        if num!=pre:
            pre=num
            newrank.append(num)
    ranked=newrank
        
    # already sorted, later bigger than formor, not be affected
    # if num>ranked[i]:
    # ranked.insert(i,num)
    print(ranked)
    res=[]
    i=len(ranked)-1
    for num in player: # >=0
        while i>=0 and ranked[i]<num: # wait for ranked>=num
            i -=1
        print(ranked[i],num,i)
        if i==-1:
            res.append(1)
        else:
            if ranked[i]==num:
                res.append(i+1)
            elif ranked[i]>num:
                res.append(i+1+1)
        
    return res
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
