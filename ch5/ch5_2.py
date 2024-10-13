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

    def insert(self, pos, item):
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
                self.size += 1
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
        if self.isEmpty() or abs(pos) > self.size-1:
            return 'Out of Range'
        else:
            if pos < 0:
                cur = self.tail
                for i in range(abs(pos)-1):
                    cur = cur.previous
            else:
                cur = self.head
                for i in range(pos+1):
                    cur = cur.next
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            self.size -= 1
            return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())