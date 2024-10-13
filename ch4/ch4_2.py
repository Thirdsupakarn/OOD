class Queue:
    def __init__(self,list = None,num = None) :
        if list == None:
            self.list = []
        else:
            self.list = list

        self.length = num
    
    def enqueue(self,data):
        self.list.append(data)
    
    def dequeue(self):
        return self.list.pop(0)

    def isEmpty(self):
        return self.list == []
    
    def isFull(self):
        return len(self.list) == self.length
    
    def size(self):
        return len(self.list)

x = [e for e in input("Enter people : ")]
main_line = Queue(x,len(x))
cashier_1 = Queue(None,5)
cashier_2 = Queue(None,5)
timer_1 = 1
timer_2 = 1 

for i in range(1,len(main_line.list)+1):
    if not cashier_1.isEmpty():
        timer_1 +=1
        if timer_1 > 3:
            cashier_1.dequeue()
            timer_1 = 1

    if not cashier_2.isEmpty(): 
        timer_2 +=1 
        if timer_2 > 2:
            cashier_2.dequeue()
            timer_2 = 1

    if not cashier_1.isFull():
        cashier_1.enqueue(main_line.dequeue())
    elif not cashier_2.isFull() and cashier_1.isFull():
        cashier_2.enqueue(main_line.dequeue())
    
    print(f"{i} {main_line.list} {cashier_1.list} {cashier_2.list}")