class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        result = []
        cur = self.head
        for i in range(self.size):
            result.append(cur.data)
            cur = cur.next
        return f'link list : {"->".join(result)}'

    def append(self, data, at_end=True):
        if self.head is None:
            self.head = Node(data)
        else:
            if at_end:
                n = self.head
                while n.next:
                    n = n.next
                n.next = Node(data)
            else:
                n = Node(data)
                n.next = self.head
                self.head = n
        self.size += 1

    def pop_head(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            return head.data
        self.size -= 1
        return None

    def pop_last(self):
        p = self.head
        while p.next is not None and p.next.next is not None:
            p = p.next
        p.next = None
        self.size -= 1
        

input_data = input("Enter Input : ").split()
ll = LinkedList()
for num in input_data:
    ll.append(num)

print(ll)
ll.pop_last()
print(ll)
