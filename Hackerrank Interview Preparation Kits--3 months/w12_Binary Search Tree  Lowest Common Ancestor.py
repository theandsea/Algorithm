# https://www.hackerrank.com/challenges/three-month-preparation-kit-binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def contain(root,v):
    if root is None: # None first judged !!!
        return False
    elif root.info==v:
        return True
    elif root.left is not None and contain(root.left,v):
        return True
    elif root.right is not None and contain(root.right,v):
        return True
    else:
        return False

def lca(root, v1, v2):  # type of v1,v2 ... integer
    #Enter your code here
    if root==v1 or root==v2:
        return root
    elif root.right is not None and contain(root.right,v1) and contain(root.right,v2):
        return lca(root.right,v1,v2)
    elif root.left is not None and contain(root.left,v1) and contain(root.left,v2):
        return lca(root.left,v1,v2)
    else:
        return root
            
  

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
