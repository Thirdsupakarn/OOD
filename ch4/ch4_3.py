class Queue():
    def __init__(self,code):
        self.code = code.replace(' ','')
        self.lst = [i for i in self.code]

    def enqueue(self,inp):
        self.lst.append(inp)

    def dequeue(self):
        return self.lst.pop(0)

    def items(self):
        return self.code

    def size(self):
        return len(self.code)

def encodemsg(a,b):
    result = []
    for i in range(len(a.lst)):
        b.enqueue(b.lst[i])
        newchr = ord(a.lst[i])+int(b.lst[i])
        if a.lst[i].isupper():
            if newchr <= ord('Z'):
                result.append(chr(newchr))
            else:
                temp = newchr - ord('Z')
                while temp > ord('Z'):
                    temp = temp - ord('Z')
                result.append(chr(temp+ord('A')-1))
        elif a.lst[i].islower():
            if newchr <= ord('z'):
                result.append(chr(newchr))
            else:
                temp = newchr - ord('z')
                while temp > ord('z'):
                    temp = temp - ord('z')
                result.append(chr(temp+ord('a')-1))
    a.lst = result
    return result
    
def decodemsg(a,b):
    result = []
    for i in range(len(a.lst)):
        newchr = ord(a.lst[i])-int(b.lst[i])
        if a.lst[i].isupper():
            if newchr >= ord('A'):
                result.append(chr(newchr))
            else:
                temp = ord('A') - newchr
                result.append(chr(ord('Z')-temp+1))
        elif a.lst[i].islower():
            if newchr >= ord('a'):
                result.append(chr(newchr))
            else:
                temp = ord('a') - newchr
                result.append(chr(ord('z')-temp+1))
    return result  

x = input("Enter String and Code : ").split(',')
string,number = x[0],x[1]
q1 = Queue(string)
q2 = Queue(number)

print(f"Encode message is : {encodemsg(q1, q2)}")
print(f"Decode message is : {decodemsg(q1, q2)}")