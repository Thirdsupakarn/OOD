inp, worker = input("Enter jobs and number of workers : ").split('/')
inp = [int(e) for e in inp.split()]
load = [0]*int(worker)

for i in range(len(inp)-1,-1,-1):
    load[load.index(min(load))]+=inp[i]
    print(f'{inp[i]} added to index {load.index(min(load))}')

print(min(load))