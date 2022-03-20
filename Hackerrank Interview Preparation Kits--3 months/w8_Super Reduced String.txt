# https://www.hackerrank.com/challenges/three-month-preparation-kit-reduced-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eight
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    # just use a stack---> similar to calculator....no need for nex array
    # because of the stucture of nearest matching
    st=[]
    for lt in s:
        if len(st)>0:
            if lt == st[-1]:
                st.pop()
            else:
                st.append(lt)
        else:
            st.append(lt)
    
    if len(st) > 0:
        return "".join(st)
    else:
        return "Empty String"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
