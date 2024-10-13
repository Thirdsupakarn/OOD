class Node:
    def __init__(self, previous = None, data = None, next = None):
        self.previous = previous
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        create = Node()
        self.head = create
        self.tail = create
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        s = ''
        for i in range(self.size):
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur =  self.tail
        s = ''
        for i in range(self.size):
            s += str(cur.previous.data) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, item):
        addT = Node(None, item, None)
        temp = self.tail.previous
        self.tail.previous = addT
        addT.previous = temp
        temp.next = addT
        addT.next = self.tail
        self.size += 1

    def addHead(self, item):
        addH = Node(None, item, None)
        temp = self.head.next
        self.head.next = addH
        addH.next = temp
        temp.previous = addH
        addH.previous = self.head
        self.size += 1

    def insert(self, pos , item):
        ins = Node(None, item, None)
        if pos > self.size:
            self.append(item)
        elif pos < 0:
            if abs(pos) > self.size:
                self.addHead(item)
            else:
                cur = self.tail
                for i in range(abs(pos)):
                    cur = cur.previous

                temp = cur.previous
                cur.previous = ins
                ins.previous = temp
                ins.next = cur
                temp.next = ins
        else:
            cur = self.head
            for i in range(pos):
                cur = cur.next

            temp = cur.next
            cur.next = ins
            ins.previous = cur
            ins.next = temp
            temp.previous = ins
        self.size += 1

    def search(self, item):
        cur = self.head
        for i in range(self.size):
            cur = cur.next
            if cur.data == item:
                return 'Found'
        return 'Not Found'

    def index(self, item):
        cur = self.head
        for i in range(self.size):
            cur = cur.next
            if cur.data == item:
                return i
        return -1
    
    def size(self):
        return self.size

    def pop(self, pos):
        if self.isEmpty() or abs(pos) > self.size:
            return 'Out of Range'
        else:
            if pos < 0:
                cur = self.tail
                for i in range(abs(pos)):
                    cur = cur.previous
            else:
                cur = self.head
                for i in range(pos+1):
                    cur = cur.next
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            self.size -= 1
            return 'Success'
    
    def moveL(self):
        cur = self.head
        if cur.next.data == '|':
            return
        while cur.next is not None:
            cur = cur.next
            if cur.data == '|':
                if cur.previous != self.head: 
                    temp = cur
                    cur = cur.previous
                    cur.next = temp.next
                    temp.next.previous = cur
    
                    temp.next = cur
                    temp.previous = cur.previous
                    cur.previous.next = temp
                    cur.previous = temp

                    if self.head.next == cur:
                        self.head.next = temp
                    if self.tail.previous == temp:
                        self.tail.previous = cur
                    break

    def moveR(self):
        cur = self.head
        if self.tail.previous.data == '|':
            return
        while cur.next is not None:
            cur = cur.next
            if cur.data == '|':
                if cur.next != self.tail: 
                    temp = cur
                    cur = cur.next
                    cur.previous = temp.previous
                    temp.previous.next = cur
                    
                    temp.previous = cur
                    temp.next = cur.next
                    cur.next.previous = temp
                    cur.next = temp

                    if self.head.next == temp:
                        self.head.next = cur
                    if self.tail.previous == cur:
                        self.tail.previous = temp
                    break  

    def delWordLeft(self):
        if self.head.next.data == '|':
            return
        temp = self.index('|')-1
        self.pop(temp)

    def delWordRight(self):
        if self.tail.previous.data == '|':
            return
        temp = self.index('|')+1
        self.pop(temp)

L = LinkedList()
inp = input('Enter Input : ').split(',')
L.append('|')
for i in inp:
    if i[:1] == 'I':
        temp = L.index('|')
        L.pop(temp)
        L.insert(temp,i[2:])
        L.insert(temp+1,'|')
    elif i[:1] == 'L':
        L.moveL()
    elif i[:1] == 'R':
        L.moveR()
    elif i[:1] == 'B':
        L.delWordLeft()
    elif i[:1] == 'D':
        L.delWordRight()

print(L)