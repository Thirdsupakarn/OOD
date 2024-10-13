class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        create = Node()
        self.head = create
        self.tail = create
        self.size = 0

    def __str__(self):
        result = []
        cur = self.head.next
        for i in range(self.size):
            result.append(cur.data)
            cur = cur.next
        return f'link list : {"->".join(result)}'

    def append(self, data):
        temp = Node(data)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def isEmpty(self):
        return self.size == 0
    
    def insert(self, index, data):
        cur = self.head
        temp = Node(data)
        if index < 0 or index > self.size:
            return "Data cannot be added"
        
        for i in range(index):
            cur = cur.next

        temp2 = cur.next
        cur.next = temp
        temp.next = temp2 
        self.size +=1
        return f"index = {index} and data = {data}"   

x = input("Enter Input : ").split(",")
lst = x[0].split()
x.remove(x[0])
x = [[j.strip() for j in e.split(":")] for e in x]
linklst = LinkedList()

for i in lst:
    linklst.append(i)


print("List is empty" if linklst.isEmpty() else linklst)

for i in x:
    print(linklst.insert(int(i[0]),i[1]))
    print("List is empty" if linklst.isEmpty() else linklst)
    
    



