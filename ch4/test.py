class Queue: 
    def __init__(self,inp = []):
        self.items = inp
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        return self.items.popleft()
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

def get_number(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10   

def get_max_number(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(l) :
    result = Queue(l)
    max_number = get_max_number(max(l))
    qDigit =[Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    for i in range (1,max_number+1) :
        while not result.isEmpty() :
            num = result.deQueue()
            num_number = get_number(num,i)
            qDigit[num_number].enQueue(num)
    for i in range (10) :
        while not qDigit[i].isEmpty() :
            result.enQueue(qDigit[i].deQueue())
    return result.item


