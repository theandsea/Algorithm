# https://www.hackerrank.com/challenges/three-month-preparation-kit-merging-communities/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
# Enter your code here. Read input from STDIN. Print output to STDOUT

# since update, must use Union Find

par=[] # direct parent of each node
sn=[] # size of that tree
def root(x):
    # find the root of x
    # also try to restruct to improve performance
    st=[]
    curr=x
    while not (par[curr] == curr):
        st.append(curr)
        curr=par[curr]
    while len(st)>0:
        p=st.pop()
        par[p]=curr
        
    return curr
    
def query(cmd): 
    # execute the query for each step
    # M x y....Q x
    para=cmd.split(' ')
    if para[0]=='M':
        a=int(para[1])
        b=int(para[2])
        root_a=root(a)
        root_b=root(b)
        if root_a!=root_b:
            par[root_b]=root_a
            sn[root_a] += sn[root_b]
    elif para[0]=='Q':
        x=int(para[1])
        print(sn[root(x)])


cmd=input().rstrip().split(' ')
n=int(cmd[0])
q=int(cmd[1])
par=[i for i in range(n+1)]
sn=[1 for i in range(n+1)]
for i in range(q):
    cmd=input().rstrip()
    query(cmd)
    
