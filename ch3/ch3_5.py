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
    

print("******** Parking Lot ********")

m,car_in_soi,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
if car_in_soi == '0':
    lst = None
else:
    lst = [int(e) for e in car_in_soi.split(",")]

s = Stack(lst)
i = 0
if o == 'arrive':
    if s.size() == m:
        print(f"car {n} cannot arrive : Soi Full")
    elif n in s.list:
        print(f"car {n} already in soi")
    else:
        s.push(n)
        print(f"car {n} arrive! : Add Car {n}")

elif o == 'depart':
    if s.isEmpty():
        print(f"car {n} cannot depart : Soi Empty")
    elif n in s.list:
        while i < s.size():
            if s.list[i] == n:
                s.list.pop(i)
                print(f"car {n} depart ! : Car {n} was remove")
                break
            i+=1 
    else:
        print(f"car {n} cannot depart : Dont Have Car {n}")

print(s.list)