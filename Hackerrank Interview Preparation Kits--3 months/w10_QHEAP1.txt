# https://www.hackerrank.com/challenges/three-month-preparation-kit-qheap1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-ten
# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq as hp

Q=int(input().rstrip())
A=[]
delete={} # by dictionary...
for i in range(Q):
    cmd=input().rstrip().split(" ")
    # print(cmd)
    if cmd[0]=='1': # insert
        hp.heappush(A,int(cmd[1]))
    elif cmd[0]=='2': # delete
        if cmd[1] in delete:
            delete[int(cmd[1])] += 1
        else:
            delete[int(cmd[1])] =1
    elif cmd[0]=='3': # print
        while A[0] in delete:
            delete[A[0]] -= 1
            if delete[A[0]]==0:
                delete.pop(A[0])
            hp.heappop(A)
        print(A[0])
        
