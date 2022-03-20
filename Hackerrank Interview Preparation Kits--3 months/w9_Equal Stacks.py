# https://www.hackerrank.com/challenges/three-month-preparation-kit-equal-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    # just find the entry of 3 cylinder
    h=[h1,h2,h3]
    highest=0
    times=[0 for i in range(10000010)]
    for cylinder in h:
        pres=0
        for i in reversed(range(len(cylinder))): # reversed!!!!!!!!!!read with example, sometimes nuance ruin the solution !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            pres += cylinder[i]
            times[pres] += 1
            # print(cylinder[i],times[:10])
            if times[pres] == 3 and highest<pres:
                highest=pres
    
    return highest
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
