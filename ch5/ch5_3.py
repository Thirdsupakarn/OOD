class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        create = Node()
        self.head = create
        self.size = 0
        self.sort_status = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        if self.sort_status == 0:
            s = 'Before: '
        else:
            s = 'After : '
        for i in range(self.size):
            s += str(cur.next.data) 
            if i != self.size-1:
                s += " -> "
            cur = cur.next
        return s
    
    def isEmpty(self):
        return self.size == 0
    
    def append(self, data):
        temp = Node(data)
        cur = self.head
        for i in range(self.size):
            cur = cur.next
        
        cur.next = temp
        self.size += 1

    def sort(self):        
        cur = self.head.next
        while cur.next is not None:
            point = cur.next
            while point is not None:
                if cur.data > point.data:
                    cur.data, point.data = point.data, cur.data
                point = point.next
            
            cur = cur.next
        
        self.sort_status = 1
     
inp = input('Enter unsorted Linked List: ').split()
L = LinkedList()
for i in inp:
    L.append(i)

print(L)
L.sort()
print(L)

