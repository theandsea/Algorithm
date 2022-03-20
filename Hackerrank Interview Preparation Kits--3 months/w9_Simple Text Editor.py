# https://www.hackerrank.com/challenges/three-month-preparation-kit-simple-text-editor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
# Enter your code here. Read input from STDIN. Print output to STDOUT

class editor:
    def __init__(self):
        self.st=[] # for undo
        self.s=""
        
    def append(self,w): # 1
        assert isinstance(w,str)
        self.s += w
    
    def delete(self,k): # 2
        assert isinstance(k,int) and k>0
        self.s = self.s[:-k]
    
    def print(self,k): # 3
        assert isinstance(k,int) and 1<=k<=len(self.s) # 1-indexed
        print(self.s[k-1])
    
    def undo(self): # 4
        assert len(self.st)>0
        # print(self.st)
        (t,para)=self.st.pop()
        if t==1:
            self.append(para)
        elif t==2:
            self.delete(para)
        
        
    
Q=int(input())
ed=editor()
for i in range(Q):
    # print("=======================")
    cmd=input()
    t=int(cmd[0]) # type
    if t==1:
        w=cmd[2:]
        # record
        ed.st.append((2,len(w)))
        ed.append(w)
    elif t==2:
        k=int(cmd[2:])
        # record
        ed.st.append((1,ed.s[-k:]))
        ed.delete(k)
    elif t==3:
        k=int(cmd[2:])
        ed.print(k)
    elif t==4:
        ed.undo()
    # print(cmd,"\t",ed.s)
