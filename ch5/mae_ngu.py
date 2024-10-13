class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        p = self.head
        result = f'({p.data})'
        if p.next == None:
            return result + '->Empty'
        while p.next != None:
            p = p.next
            result += '->' + str(p.data)
        return result
    
    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
        self.size += 1
        
    def isEmpty(self):
        return self.size == 0 or self.head == None
    
    def sum(self):
        result = 0
        p = self.head
        while p != None:
            result += p.data
            p = p.next
        return result
        
    def shake(self):
        shaked_snake = LinkedList()
        if self.isEmpty() or self.head.next == None:
            return shaked_snake
        
        prev = self.head
        cur = prev.next
        while cur != None:
            if cur.data > self.head.data:
                shaked_snake.append(cur.data)
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                self.size -= 1
            else:
                prev = cur
            cur = prev.next
        return shaked_snake
    
    def swap(self, e1, e2):
        e1.data, e2.data = e2.data, e1.data
    
    def play(self, snake_size):
        dead_snake = LinkedList()
        if self.sum() >= snake_size:
            return dead_snake
        
        little_snake = None
        p = self.head
        while p != None:
            if p.data != 0 and snake_size % p.data == 0 :
                little_snake = p
            p = p.next 
        
        if little_snake == None:
            self.swap(self.tail, self.head)
        else:
            s = little_snake.next
            while s != None:
                dead_snake.append(s.data)
                self.size -= 1
                if s == self.tail:
                    break
                s = s.next
            little_snake.next = None
            self.tail = little_snake
            if self.size == 1:
                return 'Mom is dead'
        return dead_snake
    
    def printList(self):
        if self.isEmpty():
            return '[]'
        result = ''
        p = self.head
        while p.next != None:
            result += str(p.data) + ', '
            p = p.next
        result += str(p.data)
        return f'[{result}]'
    
################################################################################################################

l = LinkedList()
inp, operation = input('Snake Game : ').split('/')
operation = operation.split(',')
for i in inp.split():
    l.append(i)
print(l)

for op in operation:
    if l.size == 1:
        print('Mom is dead')
        break
    if op[0] == 'D':
        result = l.play(int(op[2:]))
        if result == 'Mom is dead':
            print(result)
            break
        else:
            print(f'Play success!->{result.printList()}', l, sep = '\n')
    elif op == 'SH':
        result = l.shake()
        print(f'Shake success!->{result.printList()}', l, sep = '\n')
    elif op == 'SW':
        prev = l.head
        cur = l.head.next
        if l.size >= 2:
            while cur != None and cur.next != None:
                l.swap(cur, cur.next)
                prev = cur.next
                cur = prev.next
        if cur != None:
            prev.next = None
            l.tail = prev
            l.size -= 1
        print('Swap success!', l, sep = '\n')
    elif op[0] == 'F':
        l.append(op[2:])
        print(f'Steal success!->{op[2:]}', l, sep = '\n')
    print('------------------------------')
    if l.size == 1:
        print('Mom is dead')
        break
print('Snake Game :')