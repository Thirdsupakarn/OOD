class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendHead(self,value):
        self.head = self.tail = Node(value)

    def appendLast(self,value):
        self.size += 1
        if self.head is None:
            self.appendHead(value)
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def removeLast(self):
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        elif self.size > 1:
            now = self.head
            while now.next != self.tail:
                now = now.next
            now.next = None
            self.tail = now
            self.size -= 1
        else :
            print("Error!!!")

    def rename(self, newName):
        if self.size == 0:
            print("Error!!!")
            return
        self.tail.value = newName

    def printList(self):
        if self.size == 0:
            print("Linklist is empty!")
            return
        s = ""
        now = self.head
        for i in range(self.size-1):
            s += now.value + " -> "
            now = now.next
        s += now.value
        print(s)

    def printListWithNoDuplicate(self):
        if self.size == 0:
            print("Linklist is empty!")
            return
        s = ""
        now = self.head
        for i in range(self.size-1):
            if now.value not in s:
                s += now.value + " -> "
            now = now.next
        if now.value not in s:
            s += now.value
        else :
            s = s[:-4]
        print(s)


def convertToLinkList(ls):
    ans = List()
    for i in ls:
        ans.appendLast(i)
    return ans


print("*** My Favourite Keynote ***")
inputl = input("Enter Input / List of operation : ").split('/')
listSong = [ele for ele in inputl[0].strip().split(' ')]
operations = [ele for ele in inputl[1].strip().split(", ")]
myLinkList = convertToLinkList(listSong)
myLinkList.printList()
for i in operations:
    if i[0] == 'D':
        myLinkList.removeLast()
    elif i[0] == 'R':
        myLinkList.rename(i[2:])
    else :
        myLinkList.appendLast(i[2:])
myLinkList.printList()
myLinkList.printListWithNoDuplicate()