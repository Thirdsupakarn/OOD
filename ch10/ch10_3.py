class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self,size,maxColl):
        self.size = size
        self.maxColl = maxColl
        self.table = [None for i in range(tSize)]

    def is_full(self):
        if not None in self.table:
            print("This table is full !!!!!!")
            exit()

    def insert(self, key, val):
            self.is_full()
            coll = 0
            bIdx = idx = sum(ord(i) for i in key)%self.size
            while self.table[idx]:
                coll+=1
                print(f"collision number {coll} at {idx}")
                if coll == self.maxColl:
                    print("Max of collisionChain")
                    break
                idx = (bIdx+(coll**2))%self.size
            if not self.table[idx]:
                self.table[idx] = Data(key,val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "---------------------------"



print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')
tSize, maxColl = int(inp[0].split()[0]),int(inp[0].split()[1])
hash = Hash(tSize,maxColl)
for i in inp[1].split(','):
    key, val = i.split()
    hash.insert(key,val) or print(hash)