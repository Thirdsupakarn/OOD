class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self,data):
        self.root  = BST._insert(self.root,data)
        return self.root

    def _insert(node:Node,data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left =  BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def checkpos(self,inp):
        if self.root.data == inp:
            return 'Root'  
        cur = self.root
        while cur is not None:
            if inp < self.root.data and cur.left is not None:
                cur = cur.left
            elif inp > self.root.data and cur.right is not None:
                cur = cur.right
            else:
                return 'Not exist'
                
            if cur.data == inp:
                if  cur.left is None and cur.right is None:
                    return 'Leaf'
                else:
                    return 'Inner'

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(inp[0]))