# https://www.hackerrank.com/challenges/three-month-preparation-kit-queue-using-two-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eight
# Enter your code here. Read input from STDIN. Print output to STDOUT

# using a stack to implement

class que:
    def __init__(self,data=None):
        self.q=[] # using a stack
        self.f=0 # front, included
        # self.e=0 # end=len(q), not included
        if data is not None:
            self.enqueue(data)
    
    def enqueue(self,data):
        self.q.append(data)
    
    def deque(self):
        if self.unempty():
            obj=self.q[self.f]
            self.f += 1
            if self.f>=10000: # delete it 
                self.q=self.q[self.f:]
                self.f=0
            return obj
        else:
            return "error"
    
    def pr_fr(self):
        if self.unempty():
            return self.q[self.f]
            
    def unempty(self):
        if self.f < len(self.q):
            return True
        else:
            return False
        
        
q=int(input())
myq=que()
for i in range(q):
    cmd=input().strip()
    t=int(cmd[0])
    if t==1:
        num=int(cmd[2:])
        myq.enqueue(num)
    elif t==2:
        myq.deque()
    elif t==3:
        print(myq.pr_fr())
    #print(i)
    #print(myq.q,myq.f)

