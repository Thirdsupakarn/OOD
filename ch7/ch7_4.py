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

    def preorder(node:Node):
        if node is None:
            return []
        return ([str(node.data)]) + BST.preorder(node.left) + BST.preorder(node.right)

    def inorder(node:Node):
        if node is None:
            return []
        return  BST.inorder(node.left) + ([str(node.data)]) + BST.inorder(node.right)

    def postorder(node:Node):
        if node is None:
            return []
        return  BST.postorder(node.left) + BST.postorder(node.right) + ([str(node.data)])

    def breadth(node:Node):
        if node is None:
            return ''
        result = [node]
        for n in result:
            if n.left is not None:
                result.append(n.left)
            if n.right is not None:
                result.append(n.right)
        return ' '.join([str(e) for e in result])
            


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(f'Preorder : {" ".join(BST.preorder(root))}')
print(f'Inorder : {" ".join(BST.inorder(root))}')
print(f'Postorder : {" ".join(BST.postorder(root))}')
print(f'Breadth : {BST.breadth(root)}')