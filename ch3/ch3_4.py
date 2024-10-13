class Stack :
    def __init__(self,list = None) :
        if list == None:
            self.list = []
        else:
            self.list = list
    def isEmpty(self) :
        return self.list == []
    def push(self,data) :
        return self.list.append(data)
    def pop(self) :
        return self.list.pop()
    def size(self) :
        return len(self.list)
    def peek(self) :
        return self.list[-1]

def in_stack(x):
    switch = {
        '+': 2,
        '-': 2,
        '*': 4,
        '/': 4,
        '(': 0,
    }
    return switch.get(x)
    
def out_stack(x):
    switch = {
        '+': 1,
        '-': 1,
        '*': 3,
        '/': 3,
        '(': 100000,
    }
    return switch.get(x)

oparation = ["(","+","-","*","/"]

def infix2postfix(inp) :
    s = Stack()
    result = []
    for i in inp:
        if i == ')':
            while s.peek() != '(':
                result.append(s.pop()) 
            s.pop()
        elif i in oparation:
            if s.isEmpty() or out_stack(i) > in_stack(s.peek()):
                s.push(i)
            else:
                while not s.isEmpty() and in_stack(s.peek()) > out_stack(i):
                    result.append(s.pop()) 
                s.push(i)
        elif i not in oparation:
            result.append(i)
            

    while s.size() > 0:
        result.append(s.pop()) 

    return "".join(result)



print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))
