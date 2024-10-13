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

    def insert(self, data):
        self.root =BST._insert(self.root,data)
        return self.root

    def _insert(node:Node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_height(self):
        temp = [self.root]
        visited = set()
        max_len = 0
        while temp:
            cur = temp[-1]
            if cur.left is not None and cur.left not in visited:
                temp.append(cur.left)
            elif cur.right is not None and cur.right not in visited:
                temp.append(cur.right)
            else:
                max_len = max(len(temp),max_len)
                visited.add(temp.pop())
        return max_len-1

    def _find_height(node):
        if node is None:
            return -1
        left = BST._find_height(node.left)
        right = BST._find_height(node.right)
        return max(left,right)+1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(f'Height of this tree is : {BST._find_height(root)}')